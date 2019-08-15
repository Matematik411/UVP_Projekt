def preveri(k):
    try:
        k = int(k)
        return "je stevilo"
    except ValueError:
        return "ni stevilo"


def prestej(niz):
    print(len(niz.split()))

niz = "Vem, da nisem prvi, ki ne zna stop’t na divji vrh sveta in ne bom ta zadn, k’ te vidu v sanjah. Kolk jih je pred mano dihal’ zrak in kolkim se rodi najlepši otrok? Kolk jih še pride sem za nami v ta rod?"
prestej(niz)
import random
list = [1,2,3,4,5]
random.shuffle(list)
print(list)






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
                prava = vrstica[::]
            if i == 2 * pesem:
                avtor, naslov = vrstica.split(",")
                naslov = naslov.strip()
        return prava, avtor, naslov
a = lyrics(2,"besedila.txt",3)[0]
vse = []
niz = ""
locila = ".,!?"
for beseda in a:
    if "-" != beseda[0]:
        niz += beseda + " "
    else:
        if beseda[-1] not in locila:
            vse.append(niz)
            # da button
            niz = " "
        else:
            vse.append(niz)
            niz = beseda[-1] + " "
vse.append(niz[:-1])
print(vse)


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
            if i == 2 * pesem:
                avtor, naslov = vrstica.split(",")
                naslov = naslov.strip()
        return koncen, iskane, avtor, naslov




haha = ([3,1,2,0], ["prva", "druga", "tretja", "cetrta"])
for st in haha[0]:
    print(haha[1][st])