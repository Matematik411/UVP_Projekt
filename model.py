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
    
    def preveri_racun(self, vrednost):
        return self.resitev() == vrednost
#------------------------------------------------------------


# test = Racun(5)
# test.sestavi_racun(4)
# print(test.a)
# print(test.b)
# print(test.znak)
# print(test.resitev())



#------------------------------------------------------------
#* Razred LYRICS, za tip naloge, ko igralec ugiba izbrisane besede iz besedila pesmi.

# Funkcija, ki iz datoteke s pesmimi izbere zeljeno in izbrise nekaj besed, spremeni vse v potrebne oblike.
def lyrics(level, datoteka_s_pesmimi, pesem):
    locila = ".,!?"
    stevilo = 2 * level
    with open(datoteka_s_pesmimi, "r", encoding="utf-8") as dat:
        for i, vrstica in enumerate(dat):
            if i == 2 * pesem + 1:
                vrstica = vrstica.split()
                while stevilo > 0:
                    zamenjan = random.randint(1, len(vrstica) - 2)
                    beseda = vrstica[zamenjan]
                    if len(beseda) > 1 and "’" not in beseda and "-" != beseda[0]:
                        vrstica[zamenjan] = "-" + beseda
                        stevilo -= 1
                koncen = ""
                iskane = []
                for beseda in vrstica:
                    if beseda[0] == "-":
                        if beseda[-1] in locila:
                            koncen += "_____" + beseda[-1] + " "
                            iskane.append(beseda[1:-1].upper())
                        else:
                            koncen += "_____" + " "
                            iskane.append(beseda[1:].upper())
                    else:
                        koncen += beseda + " "
                koncen = koncen[:-1]
                prava = vrstica[::]
            if i == 2 * pesem:
                avtor, naslov = vrstica.split(",")
                naslov = naslov.strip()
        deli = []
        niz = ""
        for beseda in prava:
            if "-" != beseda[0]:
                niz += beseda + " "
            else:
                if beseda[-1] not in locila:
                    deli.append(niz)
                    niz = " "
                else:
                    deli.append(niz)
                    niz = beseda[-1] + " "
        deli.append(niz[:-1])
        return deli, iskane, avtor, naslov

class Lyrics:
    def __init__(self, level):
        self.level = level

    def sestavi_tekst(self, datoteka_s_pesmimi, pesem):
        self.koncen, self.iskane, *self.podatki = lyrics(self.level, datoteka_s_pesmimi, pesem)

    def preveri_lyrics(self, vnosi):
        return [self.iskane[i] == vnosi[i].upper() for i in range(len(self.iskane))]
#------------------------------------------------------------
    

# pesem = Lyrics(4)
# pesem.sestavi_tekst(2)
# print(pesem.koncen)
# print(pesem.iskane)
# print(pesem.podatki)
#print(pesem.preveri_lyrics(["poljuBljena", "poljuBljena", "poljuBljena", "poljuBljena", "poljuBljena", "poljuBljena"]))



#------------------------------------------------------------
#* Razred IGRALEC, ki nadzira posameznega igralca.


class Igralec:
    def __init__(self, ime, stevilo):
        self.level = 2
        self.exp = 0
        self.ime = ime
        self.preostale_pesmi = [i for i in range(stevilo)] #st pesmi

    def racunaj(self):
        racun = Racun(self.level)
        racun.sestavi_racun(random.randrange(5))
        return racun.a, racun.znak, racun.b, racun.resitev()



    def zapoj(self, datoteka_s_pesmimi):
        pesem = Lyrics(self.level)
        zap_st = random.choice(self.preostale_pesmi)
        pesem.sestavi_tekst(datoteka_s_pesmimi, zap_st)
        self.preostale_pesmi.remove(zap_st)
        return pesem.podatki, pesem.koncen, pesem.iskane


    def napredek(self, tocke):
        self.exp += tocke
        while self.exp >= 5 * self.level:
            self.exp -= 5 * self.level
            self.level += 1

#------------------------------------------------------------

# miha = Igralec("Miha")
# print(miha.racunaj())
# print(miha.zapoj())

#------------------------------------------------------------
#* Razred NADZOR, ki nadzira, shranjuje...

class Nadzor:
    def __init__(self, datoteka_s_stanjem, datoteka_s_pesmimi):
        self.igralci = {}
        self.datoteka_s_stanjem = datoteka_s_stanjem
        self.datoteka_s_pesmimi = datoteka_s_pesmimi
        self.odgovor = False
        with open(datoteka_s_pesmimi) as dat:
            for i, _ in enumerate(dat):
                pass
        self.stevilo_pesmi = (i + 1) // 2

    def nov_igralec(self, ime):
        igralec = Igralec(ime.capitalize(), self.stevilo_pesmi)
        self.igralci[ime.upper()] = igralec
        return ime.upper()


    def shrani(self):
        with open(self.datoteka_s_stanjem, "w", encoding="utf-8") as dat:
            podatki = {ime: {"level" : igralec.level, "exp" : igralec.exp,
            "pesmi" : igralec.preostale_pesmi}
            for ime, igralec in self.igralci.items()}
            json.dump(podatki, dat)


    def nalozi(self):
        with open(self.datoteka_s_stanjem, "r", encoding="utf-8") as dat:
            podatki = json.load(dat)
            for ime, slovar in podatki.items():
                igralec = Igralec(ime, self.stevilo_pesmi)
                igralec.level = slovar["level"]
                igralec.exp = slovar["exp"]
                igralec.preostale_pesmi = slovar["pesmi"]
                self.igralci[ime] = igralec

    def dodaj_pesem(self, podatki, niz):
        for igralec in self.igralci.values():
            igralec.preostale_pesmi.append(self.stevilo_pesmi)
        self.stevilo_pesmi += 1
        self.shrani()
        avtor, naslov = podatki
        with open(self.datoteka_s_pesmimi, "a", encoding="utf-8") as dat:
            print("{0}, {1}".format(avtor, naslov), file=dat)
            print(" ".join(niz.split()), file=dat)

    
     
# nadzor = Nadzor(DATOTEKA_S_STANJEM, DATOTEKA_S_PESMIMI)
# x = nadzor.nov_igralec("nejc")
# print(nadzor.igralci[x].preostale_pesmi)
# for igralec in nadzor.igralci.values():
#     igralec.preostale_pesmi.append(nadzor.stevilo_pesmi)
# pl = nadzor.igralci[x]
# print(nadzor.igralci[x].preostale_pesmi)
# print(x)
# print(nadzor.igralci[x].ime)
# print(nadzor.igralci)
# print(pl.level)
# pl.napredek(18)
# print(pl.level)
# print(pl.exp)
# print(nadzor.stevilo_pesmi)
# niz= """Ampak sem edini, k’ s tvoje rane liže kri,
# jaz sem edini, k’ tvoj jok umiri.
# In samo edini, k’ ne obstaja,
# ne obstaja brez tvojega sveta."""
# podatki = ("Siddharta","Samo edini")
# avtor, naslov = podatki
# nadzor.stevilo_pesmi += 1
# with open(DATOTEKA_S_PESMIMI, "a", encoding="utf-8") as dat:
#     print("{0}, {1}".format(avtor, naslov), file=dat)
#     print(" ".join(niz.split()), file=dat)
# nadzor.dodaj_pesem(("Siddharta","Samo edini"),niz)
