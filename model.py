import random
import json
DATOTEKA_S_STANJEM = "stanje.json"
DATOTEKA_S_PESMIMI = "besedila.txt"
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

# Funkcija, ki iz datoteke s pesmimi izbere zeljeno in izbrise nekaj besed, spremeni vse v potrebne oblike.
def lyrics(level, datoteka_s_pesmimi, pesem):
    locila = ".,!?"
    stevilo = 2 * level
    with open(datoteka_s_pesmimi, "r", encoding="utf-8") as dat:
        ze_izbrane = []
        for i, vrstica in enumerate(dat):
            if i == 2 * pesem + 1:
                vrstica = vrstica.split()
                while stevilo > 0:
                    zamenjan = random.randint(1, len(vrstica) - 2)
                    beseda = vrstica[zamenjan]
                    if len(beseda) > 1 and "-" != beseda[0]:
                        kopija = beseda[::]
                        kopija.rstrip(locila)
                        kopija = kopija.upper()
                        if kopija not in ze_izbrane:
                            vrstica[zamenjan] = "-" + beseda
                            stevilo -= 1
                            ze_izbrane.append(kopija)
                prava_vrstica = vrstica[::]
            if i == 2 * pesem:
                avtor, naslov = vrstica.split(",")
                naslov = naslov.strip()
        odseki = []
        iskane = []
        niz = ""
        for beseda in prava_vrstica:
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
        return odseki, iskane, avtor, naslov

class Lyrics:
    def __init__(self, level):
        self.level = level

    # Glavna metoda, ki sestavni besedilo, manjkajoče besede. Željene podatke shrani v atribute atribute objekta razreda Lyrics.
    def sestavi_tekst(self, datoteka_s_pesmimi, pesem):
        self.odseki, self.iskane, *self.podatki = lyrics(self.level, datoteka_s_pesmimi, pesem)

#------------------------------------------------------------
    

#------------------------------------------------------------
#* Razred BESEDILNA, za tip naloge, kjer rešujemo klasično besedilno nalogo s številsko rešitvijo.
# Naloge se tu ne izbirajo glede na level igralca, saj imajo vnaprej določeno težavnost.
class Besedilna:
    def __init__(self):
        pass
    
    # Glavna metoda, ki shrani željene vrednosti v atribute objekta.
    def sestavi_besedilno(self, datoteka_z_nalogami, naloga):
        with open(datoteka_z_nalogami, "r", encoding="utf-8") as dat:
            navodilo = ""
            prvi_del = False
            drugi_del = False
            tretji_del = False
            for vrstica in dat:
                if vrstica == "(((REŠITEV))){0}\n".format(naloga):
                    prvi_del = False

                if prvi_del:
                    navodilo += vrstica
                if drugi_del:
                    resitev = int(vrstica)
                    drugi_del = False
                if tretji_del:
                    tezavnost = int(vrstica)
                    tretji_del = False

                if vrstica == "(((ZAČETEK))){0}\n".format(naloga):
                    prvi_del = True
                elif vrstica == "(((REŠITEV))){0}\n".format(naloga):
                    drugi_del = True
                elif vrstica == "(((TEŽAVNOST))){0}\n".format(naloga):
                    tretji_del = True
            self.navodilo = navodilo[:-1]
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
    def zapoj(self, datoteka_s_pesmimi):
        pesem = Lyrics(self.level)
        zap_st = random.choice(self.preostale_pesmi)
        pesem.sestavi_tekst(datoteka_s_pesmimi, zap_st)
        self.preostale_pesmi.remove(zap_st)
        return pesem.podatki, pesem.odseki, pesem.iskane

    # Ta metoda pa se kliče pri besedilni nalogi, prav tako vrne podatke.
    def resuj(self, datoteka_z_nalogami):
        naloga = Besedilna()
        zap_st = random.choice(self.preostale_naloge)
        naloga.sestavi_besedilno(datoteka_z_nalogami, zap_st)
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
    def __init__(self, datoteka_s_stanjem, datoteka_s_pesmimi, datoteka_z_nalogami):
        self.igralci = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_s_pesmimi = datoteka_s_pesmimi
        self.datoteka_z_nalogami = datoteka_z_nalogami
        self.odgovor = False
        with open(datoteka_s_pesmimi, "r", encoding="utf-8") as dat:
            for i, _ in enumerate(dat):
                pass
        self.stevilo_pesmi = (i + 1) // 2
        with open(datoteka_z_nalogami, "r", encoding="utf-8") as dat:
            for vrstica in dat:
                if vrstica[:15] == "(((TEŽAVNOST)))":
                    skupaj = int(vrstica[15:])
        self.stevilo_nalog = skupaj + 1
            
    # Se kliče za ustvarjanje novega igralca.
    def nov_igralec(self, ime, zival):
        igralec = Igralec(ime.capitalize(), zival, self.stevilo_pesmi, self.stevilo_nalog)
        self.igralci[ime.upper()] = igralec
        return ime.upper()

    # Shrani podatke o vseh igralcih v datoteko "stanje.json".
    def shrani(self):
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as dat:
            podatki = {ime: {"level" : igralec.level, "exp" : igralec.exp,
            "pesmi" : igralec.preostale_pesmi, "naloge" : igralec.preostale_naloge,
            "zival" : igralec.zival}
            for ime, igralec in self.igralci.items()}
            json.dump(podatki, dat)

    # Naloži podatke o igralcih iz datoteke "stanje.json".
    def nalozi(self):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            podatki = json.load(dat)
            for ime, slovar in podatki.items():
                igralec = Igralec(ime, slovar["zival"], self.stevilo_pesmi, self.stevilo_nalog)
                igralec.level = slovar["level"]
                igralec.exp = slovar["exp"]
                igralec.preostale_pesmi = slovar["pesmi"]
                igralec.preostale_naloge = slovar["naloge"]
                self.igralci[ime] = igralec

    # Metoda za nalaganje nove pesmi. Vnesemo željeni del besedila ter podatke o pesmi. Podatka sta naslov in izvajalec, ki pa ne smeta vsebovati vejic.
    def dodaj_pesem(self, podatki, niz):
        for igralec in self.igralci.values():
            igralec.preostale_pesmi.append(self.stevilo_pesmi)
        self.stevilo_pesmi += 1
        self.shrani()
        avtor, naslov = podatki
        with open(self.datoteka_s_pesmimi, "a", encoding="utf-8") as dat:
            print("{0}, {1}".format(avtor, naslov), file=dat)
            print(" ".join(niz.split()), file=dat)

    # Dodajanje besedilnih nalog, s številskimi rešitvami.
    def dodaj_nalogo(self, navodilo, resitev, tezavnost):
        for igralec in self.igralci.values():
            igralec.preostale_naloge.append(self.stevilo_nalog)
        with open(self.datoteka_z_nalogami, "a", encoding="utf-8") as dat:
            print("(((ZAČETEK))){0}".format(self.stevilo_nalog), file=dat)
            print(navodilo, file=dat)
            print("(((REŠITEV))){0}".format(self.stevilo_nalog), file=dat)
            print(resitev, file=dat)
            print("(((TEŽAVNOST))){0}".format(self.stevilo_nalog), file=dat)
            print(tezavnost, file=dat)
        self.stevilo_nalog += 1
        self.shrani()
 