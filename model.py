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
def lyrics(level, pesem):
    locila = ".,!?"
    stevilo = 2 * level
    with open(DATOTEKA_S_PESMIMI, "r", encoding="utf-8") as dat:
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
            if i == 2 * pesem:
                avtor, naslov = vrstica.split(",")
                naslov = naslov.strip()
        return koncen, iskane, avtor, naslov

class Lyrics:
    def __init__(self, level):
        self.level = level

    def sestavi_tekst(self, pesem):
        self.koncen, self.iskane, *self.podatki = lyrics(self.level, pesem)

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
    def __init__(self, ime):
        self.level = 2
        self.exp = 0
        self.ime = ime
        self.preostale_pesmi = [i for i in range(5)] #st pesmi

    def racunaj(self):
        racun = Racun(self.level)
        racun.sestavi_racun(random.randrange(5))
        return racun.a, racun.znak, racun.b, racun.resitev()



    def zapoj(self):
        pesem = Lyrics(self.level)
        zap_st = random.choice(self.preostale_pesmi)
        pesem.sestavi_tekst(self.preostale_pesmi.pop(zap_st))
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

    def nov_igralec(self, ime):
        igralec = Igralec(ime.capitalize())
        self.igralci[ime.upper()] = igralec
        return ime.upper()

     
# nadzor = Nadzor(DATOTEKA_S_STANJEM, DATOTEKA_S_PESMIMI)
# x = nadzor.nov_igralec("nejc")
# pl = nadzor.igralci[x]
# print(x)
# print(nadzor.igralci[x].ime)
# print(nadzor.igralci)
# print(pl.level)
# pl.napredek(18)
# print(pl.level)
# print(pl.exp)
