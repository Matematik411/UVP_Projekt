import bottle
import ast
import model

DATOTEKA_S_STANJEM = "stanje.json"
DATOTEKA_S_PESMIMI = "besedila.txt"
SKRIVNOST = "skrivnost"
nadzor = model.Nadzor(DATOTEKA_S_STANJEM, DATOTEKA_S_PESMIMI)


@bottle.get("/")
def index():
    nadzor.nalozi()
    return bottle.template("index.tpl",
    nadzor=nadzor
    )


@bottle.post("/nov_igralec/")
def nov_igralec():
    vnos = bottle.request.forms.getunicode("ime")
    igralec = nadzor.nov_igralec(vnos)
    bottle.response.set_cookie("igralec", igralec, secret=SKRIVNOST, path = "/")
    bottle.redirect("/igra/")


@bottle.post("/izbira/")
def izbira():
    igralec = bottle.request.forms.getunicode("ime")
    bottle.response.set_cookie("igralec", igralec, secret=SKRIVNOST, path = "/")
    bottle.redirect("/igra/")
        
    



@bottle.get("/igra/")
def igra():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    return bottle.template("igra.tpl",
    ime=nadzor.igralci[igralec].ime,
    igralec=nadzor.igralci[igralec])

@bottle.post("/racun/")
def racun():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    
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
        vnos = int(bottle.request.forms.getunicode("vnos"))
        if vnos == resitev:
            nadzor.igralci[igralec].napredek(1)
            nadzor.odgovor = False
            bottle.redirect("/igra/")
        else:
            return bottle.template("racun.tpl",
            znak=znak,
            a=a,
            b=b,
            odgovor=True)



@bottle.post("/pesem/")
def pesem():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    
    if not nadzor.odgovor:
    
        vrednosti = nadzor.igralci[igralec].zapoj(nadzor.datoteka_s_pesmimi)
        (avtor, naslov), niz, besede = vrednosti
        bottle.response.set_cookie("vrednosti", str(vrednosti), secret=SKRIVNOST, path="/")
        nadzor.odgovor = True
        return bottle.template("pesem.tpl",
        avtor=avtor,
        naslov=naslov,
        niz=niz,
        odgovor=False)

    else:
        (avtor, naslov), niz, besede = ast.literal_eval(
            bottle.request.get_cookie("vrednosti", secret=SKRIVNOST))

        vnos = bottle.request.forms.getunicode("vnos")
        vnos = vnos.split(",")
        uspeh = []
        for i, prava in enumerate(besede):
            if prava == vnos[i].strip().upper():
                uspeh.append("Prav")
            else:
                uspeh.append("Narobe")
        if uspeh == ["Prav"] * nadzor.igralci[igralec].level * 2:
            nadzor.igralci[igralec].napredek(3)
            nadzor.odgovor = False
            bottle.redirect("/igra/")
        else:
            return bottle.template("pesem.tpl",
            avtor=avtor,
            naslov=naslov,
            niz=niz,
            odgovor=True,
            vnos=vnos,
            uspeh=uspeh)
            


@bottle.post("/shrani/")
def shrani():
    nadzor.shrani()
    bottle.redirect("/")

@bottle.get("/dodaj/")
def dodaj():
    return bottle.template("dodaj.tpl")

@bottle.post("/dodaj_pesem/")
def dodaj_pesem():
    avtor = bottle.request.forms.getunicode("avtor")
    naslov = bottle.request.forms.getunicode("naslov")
    besedilo = bottle.request.forms.getunicode("besedilo")
    nadzor.dodaj_pesem((avtor, naslov), besedilo)
    bottle.redirect("/")







@bottle.get("/img/<picture>/")
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')
    



bottle.run(reloader=True, debug=True)