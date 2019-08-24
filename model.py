import random
import json
#* Pozdrav!
# V tej datoteki definiram vse tipe nalog, ki so na voljo v igri.

#------------------------------------------------------------
#* Razred RACUN, za tip nalog preprostega matematicnega racuna.
class Racun:
    def __init__(self, level):
        self.level = level

    # Glavna metoda, ki zgradi racun, in v atribute a, b in znak shrani ciljne vrednosti. Le te so prirejene po smislu glede na level, ko se pojavi naloga
    def sestavi_racun(self, znak):
        a = random.randrange(self.level * 50)
        b = random.randint(1, self.level * 50)
        if self.level == 1:
            #3:2 moznosti glede (+,-)
            self.znak = znak % 2
        elif self.level <= 3:
            #level 2 ima 2:1:2 moznosti glede (+,-,*) 
            #level 3 ima 2:2:1 moznosti glede (+,-,*) 
            self.znak = (znak + self.level) % 3
        elif self.level == 4:
            self.znak = znak
        else:
            #zadnji level ima dodatni zaplet moznih negativnih stevil
            a, b = a - b, a + b
            self.znak = znak
        self.a = a
        if self.znak == 2:
            self.b = b // 2
        else:
            self.b = b

    # Vrne vrednost, ki je iskana resitev
    def resitev(self):
        if self.znak == 0:
            return self.a + self.b
        elif self.znak == 1:
            return self.a - self.b
        elif self.znak == 2:
            return self.a * self.b
        elif self.znak == 3:
            return self.a // self.b
        elif self.znak == 4:
            return self.a % self.b
    
#------------------------------------------------------------


#------------------------------------------------------------
#* Razred LYRICS, za tip naloge, ko igralec ugiba izbrisane besede iz besedila pesmi.
class Lyrics:
    def __init__(self, level):
        self.level = level

    # Glavna metoda, ki sestavi besedilo, izbere nekaj besed in jih odtrani. Željene podatke shrani v atribute atribute objekta razreda Lyrics.
    def sestavi_tekst(self, datoteka_s_stanjem, pesem):
        locila = ".,!?"
        stevilo = 2 * self.level
        with open(datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            podatki = json.load(dat)
            podatki = podatki["pesmi"]
            podatki = podatki[pesem]
            avtor = podatki["avtor"]
            naslov = podatki["naslov"]
            besedilo = podatki["besedilo"]
            besedilo = besedilo.split()

            ze_izbrane = []
            while stevilo > 0:
                zamenjan = random.randint(1, len(besedilo) - 2)
                beseda = besedilo[zamenjan]
                if len(beseda) > 1 and "-" != beseda[0]:
                    kopija = beseda[::]
                    kopija.rstrip(locila)
                    kopija.rstrip()
                    kopija = kopija.upper()
                    if kopija not in ze_izbrane:
                        besedilo[zamenjan] = "-" + beseda
                        stevilo -= 1
                        ze_izbrane.append(kopija)

            odseki = []
            iskane = []
            niz = ""
            for beseda in besedilo:
                if "-" != beseda[0]:
                    niz += beseda + " "
                else:
                    if beseda[-1] not in locila:
                        odseki.append(niz)
                        iskane.append(beseda[1:].upper())
                        niz = " "
                    else:
                        odseki.append(niz)
                        iskane.append(beseda[1:-1].upper())
                        niz = beseda[-1] + " "
            odseki.append(niz[:-1])
            premesano = [i for i in range(len(iskane))]
            random.shuffle(premesano)
        self.odseki = odseki
        self.iskane = iskane
        self.premesano = premesano
        self.podatki = avtor, naslov

#------------------------------------------------------------
    

#------------------------------------------------------------
#* Razred BESEDILNA, za tip naloge, kjer rešujemo klasično besedilno nalogo s številsko rešitvijo.
# Naloge se tu ne izbirajo glede na level igralca, saj imajo vnaprej določeno težavnost.
class Besedilna:
    def __init__(self):
        pass
    
    # Glavna metoda, ki shrani željene vrednosti v atribute objekta.
    def sestavi_besedilno(self, datoteka_s_stanjem, naloga):
        with open(datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            podatki = json.load(dat)
            podatki = podatki["besedilne"]
            podatki = podatki[naloga]
            tezavnost = podatki["tezavnost"]
            navodilo = podatki["navodilo"]
            resitev = podatki["resitev"]
            
            self.navodilo = navodilo
            self.resitev = resitev
            self.tezavnost = tezavnost
                
#------------------------------------------------------------


#------------------------------------------------------------
#* Razred IGRALEC, ki nadzira posameznega igralca.
class Igralec:
    def __init__(self, ime, zival, stevilo_pesmi, stevilo_nalog):
        self.level = 1
        self.exp = 0
        self.ime = ime
        self.zival = zival
        self.preostale_pesmi = [i for i in range(stevilo_pesmi)]
        self.preostale_naloge = [i for i in range(stevilo_nalog)]

    # To metodo se kliče za nalogo računa. Vrne podatke, za sestavo računa.
    def racunaj(self):
        racun = Racun(self.level)
        racun.sestavi_racun(random.randrange(5))
        return racun.a, racun.znak, racun.b, racun.resitev()

    # To metodo se kliče za nalogo iskanja manjkajočih besed. Vrne iskane podatke.
    def zapoj(self, datoteka_s_stanjem):
        pesem = Lyrics(self.level)
        zap_st = random.choice(self.preostale_pesmi)
        pesem.sestavi_tekst(datoteka_s_stanjem, zap_st)
        self.preostale_pesmi.remove(zap_st)
        return pesem.podatki, pesem.odseki, pesem.iskane, pesem.premesano

    # Ta metoda pa se kliče pri besedilni nalogi, prav tako vrne podatke.
    def resuj(self, datoteka_s_stanjem):
        naloga = Besedilna()
        zap_st = random.choice(self.preostale_naloge)
        naloga.sestavi_besedilno(datoteka_s_stanjem, zap_st)
        self.preostale_naloge.remove(zap_st)
        return naloga.navodilo, naloga.resitev, naloga.tezavnost

    # V primeru pravilno rešene naloge, se uporabi naslednja metoda.
    def napredek(self, tocke):
        self.exp += tocke
        while self.exp >= 4 * self.level:
            self.exp -= 4 * self.level
            self.level += 1

#------------------------------------------------------------


#------------------------------------------------------------
#* Razred NADZOR, ki nadzira, shranjuje in upravlja delovanje igre.
# Objek Nadzora ima v atributih shranjene vse potrebne podatke, za igranje in ustvarjanje novih igralcev.
class Nadzor:
    def __init__(self, datoteka_s_stanjem):
        self.igralci = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.odgovor = False
        with open(datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            podatki = json.load(dat)
            self.stevilo_pesmi = len(podatki["pesmi"])
            self.stevilo_nalog = len(podatki["besedilne"])
            
    # Se kliče za ustvarjanje novega igralca.
    def nov_igralec(self, ime, zival):
        igralec = Igralec(ime.upper(), zival, self.stevilo_pesmi, self.stevilo_nalog)
        self.igralci[ime.upper()] = igralec
        return ime.upper()

    # Shrani podatke o vseh igralcih v datoteko "stanje.json".
    def shrani(self):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            skupaj = json.load(dat)
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as dat:
            podatki = {ime.upper(): {"level" : igralec.level, "exp" : igralec.exp,
            "pesmi" : igralec.preostale_pesmi, "naloge" : igralec.preostale_naloge,
            "zival" : igralec.zival}
            for ime, igralec in self.igralci.items()}

            skupaj["igralci"] = podatki
            json.dump(skupaj, dat, indent=2)

    # Naloži podatke o igralcih iz datoteke "stanje.json".
    def nalozi(self):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            podatki = json.load(dat)["igralci"]
            for ime, slovar in podatki.items():
                igralec = Igralec(ime.upper(), slovar["zival"], self.stevilo_pesmi, self.stevilo_nalog)
                igralec.level = slovar["level"]
                igralec.exp = slovar["exp"]
                igralec.preostale_pesmi = slovar["pesmi"]
                igralec.preostale_naloge = slovar["naloge"]
                self.igralci[ime] = igralec

    # Metoda za nalaganje nove pesmi. Vnesemo željeni del besedila ter podatke o pesmi. Podatka sta naslov in izvajalec, ki pa ne smeta vsebovati vejic.
    def dodaj_pesem(self, podatki, besedilo):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            skupaj = json.load(dat)
        avtor, naslov = podatki
        pesmi = skupaj["pesmi"]
        slovar = {"avtor" : avtor, "naslov" : naslov, "besedilo": besedilo}
        pesmi.append(slovar)
        skupaj["pesmi"] = pesmi
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as dat:
            json.dump(skupaj, dat, indent=2)

        for igralec in self.igralci.values():
            igralec.preostale_pesmi.append(self.stevilo_pesmi)
        self.stevilo_pesmi += 1
        self.shrani()

    # Dodajanje besedilnih nalog, s številskimi rešitvami.
    def dodaj_nalogo(self, navodilo, resitev, tezavnost):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            skupaj = json.load(dat)
        naloge = skupaj["besedilne"]
        slovar = {"tezavnost" : tezavnost, "navodilo" : navodilo, "resitev" : resitev}
        naloge.append(slovar)
        skupaj["besedilne"] = naloge

        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as dat:
            json.dump(skupaj, dat, indent=2)
 
        for igralec in self.igralci.values():
            igralec.preostale_naloge.append(self.stevilo_nalog)
        self.stevilo_nalog += 1
        self.shrani()
