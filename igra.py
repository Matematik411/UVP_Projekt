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

@bottle.get("/racun/")
def racun():
    igralec = bottle.request.get_cookie("igralec", secret=SKRIVNOST)
    a, znak, b, resitev = nadzor.igralci[igralec].racunaj()
    bottle.response.set_cookie("resitev", resitev, secret=SKRIVNOST, path="/")
    return bottle.template("racun.tpl",
    znak=znak,
    a=a,
    b=b)














@bottle.get("/img/<picture>/")
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')
    



bottle.run(reloader=True, debug=True)