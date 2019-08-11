import bottle
import model

DATOTEKA_S_STANJEM = "stanje.json"
DATOTEKA_S_PESMIMI = "besedila.txt"
SKRIVNOST = "skrivnost"
nadzor = model.Nadzor(DATOTEKA_S_STANJEM, DATOTEKA_S_PESMIMI)


@bottle.get("/")
def index():
    return bottle.template("index.tpl")


@bottle.post("/nov_igralec/")
def nov_igralec():
    vnos = bottle.request.forms.getunicode("ime")
    igralec = nadzor.nov_igralec(vnos)
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
    
        stevila = nadzor.igralci[igralec].racunaj()
        a, znak, b, resitev = stevila
        bottle.response.set_cookie("stevila", stevila, secret=SKRIVNOST, path="/")
        nadzor.odgovor = True
        return bottle.template("racun.tpl",
        znak=znak,
        a=a,
        b=b,
        odgovor=False)

    else:
        a, znak, b, resitev = bottle.request.get_cookie("stevila", secret=SKRIVNOST)
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












@bottle.get("/img/<picture>/")
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')
    



bottle.run(reloader=True, debug=True)