import bottle
import ast
import model
import random

#* V tej datoteki, pa so še vsi ukazi, za delovanje spletnega vmesnika in upravljanja programa
# Najprej so definirane konstante, nato pa po @bottle. ukazih še dodatne strani.
# html podlaga je "base.tpl", ki se nato preko ostalih .tpl datotek razvije v spletne prikaze.

DATOTEKA_S_STANJEM = "stanje.json"
DATOTEKA_S_PESMIMI = "besedila.txt"
DATOTEKA_Z_NALOGAMI = "naloge.txt"
SKRIVNOST = "skrivnost"
nadzor = model.Nadzor(DATOTEKA_S_STANJEM, DATOTEKA_S_PESMIMI, DATOTEKA_Z_NALOGAMI)

# Prva stran
@bottle.get("/")
def index():
    nadzor.nalozi()
    return bottle.template("index.tpl",
    nadzor=nadzor,
    error=False)


# Izbira igralca preko naslednjih dveh ukazov pelje na glavno igralno stran.
@bottle.post("/nov_igralec/")
def nov_igralec():
    vnos = bottle.request.forms.getunicode("ime")
    zival = bottle.request.forms.getunicode("zival")
    if zival == "Izberi prijatelja" or len(vnos.split()) > 1 or "" == vnos or vnos.upper() in nadzor.igralci:
        return bottle.template("index.tpl",
        nadzor=nadzor,
        error=True)
    else:
        igralec = nadzor.nov_igralec(vnos, zival)
        bottle.response.set_cookie("igralec", igralec, secret=SKRIVNOST, path = "/")
        bottle.redirect("/igra/")


@bottle.post("/izbira/")
def izbira():
    igralec = bottle.request.forms.getunicode("ime")
    bottle.response.set_cookie("igralec", igralec, secret=SKRIVNOST, path = "/")
    bottle.redirect("/igra/")
        

# Stran za glavni del igre
@bottle.get("/igra/")
def igra():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    if nadzor.igralci[igralec].level == 6:
        return bottle.template("zmaga.tpl",
        igralec=nadzor.igralci[igralec])
    else:
        return bottle.template("igra.tpl",
        igralec=nadzor.igralci[igralec],
        error=False)

# Reševanje računske naloge
@bottle.post("/racun/")
def racun():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    try:
        if not nadzor.odgovor:
            vrednosti = nadzor.igralci[igralec].racunaj()
            a, znak, b, resitev = vrednosti
            bottle.response.set_cookie("vrednosti", str(vrednosti), secret=SKRIVNOST, path="/")
            nadzor.odgovor = True
            return bottle.template("racun.tpl",
            znak=znak,
            a=a,
            b=b,
            odgovor=False)

        else:
            a, znak, b, resitev = ast.literal_eval(
                bottle.request.get_cookie("vrednosti", secret=SKRIVNOST))
            vnos = bottle.request.forms.getunicode("vnos")
            try:
                vnos = int(vnos)
                if vnos == resitev:
                    nadzor.igralci[igralec].napredek(1)
                    nadzor.odgovor = False
                    bottle.redirect("/igra/")
                else:
                    return bottle.template("racun.tpl",
                    znak=znak,
                    a=a,
                    b=b,
                    odgovor=True,
                    error=False)
            except ValueError:
                return bottle.template("racun.tpl",
                znak=znak,
                a=a,
                b=b,
                odgovor=True,
                error=True)
    except (TypeError, ValueError, AttributeError):
        nadzor.odgovor = False
        return bottle.template("igra.tpl",
        igralec=nadzor.igralci[igralec],
        error=True)


# Reševanje dopolnjevanja besedila pesmi
@bottle.post("/pesem/")
def pesem():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    try:
        if not nadzor.odgovor:
            vrednosti = nadzor.igralci[igralec].zapoj(nadzor.datoteka_s_pesmimi)
            (avtor, naslov), odseki, iskane = vrednosti
            premesano = [i for i in range(len(iskane))]
            random.shuffle(premesano)
            vrednosti = ((avtor, naslov), odseki, iskane, premesano)
            bottle.response.set_cookie("vrednosti", str(vrednosti), secret=SKRIVNOST, path="/")
            nadzor.odgovor = True

            return bottle.template("pesem.tpl",
            avtor=avtor,
            naslov=naslov,
            odseki=odseki,
            premesano=(premesano, iskane),
            odgovor=False)

        else:
            (avtor, naslov), odseki, iskane, premesano = ast.literal_eval(
                bottle.request.get_cookie("vrednosti", secret=SKRIVNOST))
            vnos = [bottle.request.forms.getunicode(str(i)) for i in range(len(iskane))]
            if vnos == [None] * 2 * nadzor.igralci[igralec].level:
                raise ValueError
            uspeh = []
            for i in range(len(iskane)):
                if vnos[i] != str(i):
                    uspeh.append("narobe, ")
                else:
                    uspeh.append("prav - {0}, ".format(iskane[i]))
            uspeh[-1] = uspeh[-1][:-2]
            if vnos == [str(i) for i in range(len(iskane))]:
                nadzor.igralci[igralec].napredek(3)
                nadzor.odgovor = False
                bottle.redirect("/igra/")
            else:
                return bottle.template("pesem.tpl",
                avtor=avtor,
                naslov=naslov,
                odseki=odseki,
                premesano=(premesano, iskane),
                odgovor=True,
                vnos=vnos,
                uspeh=uspeh)
    except (TypeError, ValueError, AttributeError):
        nadzor.odgovor = False
        return bottle.template("igra.tpl",
        igralec=nadzor.igralci[igralec],
        error=True)


# Reševanje besedilnih nalog
@bottle.post("/besedilna/")
def besedilna():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    try:
        if not nadzor.odgovor:
            vrednosti = nadzor.igralci[igralec].resuj(nadzor.datoteka_z_nalogami)
            navodilo, resitev, tezavnost = vrednosti
            nadzor.odgovor = True
            bottle.response.set_cookie("vrednosti", str(vrednosti), secret=SKRIVNOST, path="/")

            return bottle.template("besedilna.tpl",
            navodilo=navodilo,
            tezavnost=tezavnost,
            odgovor=False)

        else:
            navodilo, resitev, tezavnost = ast.literal_eval(bottle.request.get_cookie("vrednosti", secret=SKRIVNOST))
            vnos = bottle.request.forms.getunicode("vnos")
            try:
                vnos = int(vnos)
                if vnos == int(resitev):
                    nadzor.igralci[igralec].napredek(int(tezavnost))
                    nadzor.odgovor = False
                    bottle.redirect("/igra/")
                else:
                    return bottle.template("besedilna.tpl",
                    navodilo=navodilo,
                    tezavnost=tezavnost,
                    odgovor=True,
                    error=False)
            except ValueError:
                return bottle.template("besedilna.tpl",
                navodilo=navodilo,
                tezavnost=tezavnost,
                odgovor=True,
                error=True)
    except (TypeError, ValueError, AttributeError):
        nadzor.odgovor = False
        return bottle.template("igra.tpl",
        igralec=nadzor.igralci[igralec],
        error=True)


# Shranjevanje profila
@bottle.post("/shrani/")
def shrani():
    nadzor.shrani()
    bottle.redirect("/")


# Če je naloga pretežka
@bottle.post("/poraz/")
def poraz():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    nadzor.igralci[igralec].napredek(-1)
    nadzor.odgovor = False
    return bottle.template("igra.tpl",
    igralec=nadzor.igralci[igralec],
    error=False)


# Naslednji trije za dodajanje nalog
@bottle.get("/dodaj/")
def dodaj():
    return bottle.template("dodaj.tpl",
    error=False)


@bottle.post("/dodaj_pesem/")
def dodaj_pesem():
    try:
        avtor = bottle.request.forms.getunicode("avtor")
        naslov = bottle.request.forms.getunicode("naslov")
        besedilo = bottle.request.forms.getunicode("besedilo")
        dolzina = len(besedilo.split())
        if "," in avtor or "," in naslov or "" in [avtor, naslov, besedilo] or 20 > dolzina or 50 < dolzina:
            raise ValueError
        nadzor.dodaj_pesem((avtor, naslov), besedilo)
        bottle.redirect("/")
    except ValueError:
        return bottle.template("dodaj.tpl",
        error=True)


@bottle.post("/dodaj_nalogo/")
def dodaj_nalogo():
    try:
        navodilo = bottle.request.forms.getunicode("navodilo")
        resitev = int(bottle.request.forms.getunicode("resitev"))
        tezavnost = int(bottle.request.forms.getunicode("tezavnost"))
        if "" in [navodilo, resitev, tezavnost] or 1 > tezavnost or 5 < tezavnost:
            raise ValueError
        nadzor.dodaj_nalogo(navodilo, resitev, tezavnost)
        bottle.redirect("/")
    except ValueError:
        return bottle.template("dodaj.tpl",
        error=True)


# Za dodajanje slik
@bottle.get("/img/<picture>/")
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')
    

bottle.run(reloader=True, debug=True)

