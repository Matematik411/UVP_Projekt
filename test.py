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






haha = ([3,1,2,0], ["prva", "druga", "tretja", "cetrta"])
for st in haha[0]:
    print(haha[1][st])

line = "01234567"
print(line[5:])

resitev = "asd"
resitev = resitev.upper()
print(resitev)