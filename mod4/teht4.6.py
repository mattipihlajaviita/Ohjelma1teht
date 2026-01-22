#annetaan koneelle matikka ja arpakone
import math
import random

#annetaan muuttujille arvot
kerrat = 0

#pisteiden kokonaismäärä
N = 1000000

#ympyrän pinta-ala
A_area = math.pi * 1 ** 2

#neliön pinta-ala
B_area = 2 * 2

#ympyrän sisälle osuvien pisteiden määrä
n_osumat = 0

#luodaan silmukka joka päättyy kun se on mennyt N kertaa läpi
while kerrat != N:

    #ohjelma ampuu pisteen 0 ja neliön pinta-alan välille + lisätään 1 "kerrat"
    piste = random.uniform(0, B_area)
    kerrat = kerrat + 1

    #jos piste osuu myös ympyrän sisälle: lisätään 1 "n_osumat"
    if  piste >= B_area-A_area:
        n_osumat = n_osumat + 1

#kun kerrat = N, ohjelma tulostaa piin likiarvon
print(f'Piin likiarvo kahden desimaalin tarkkuudella: {4*n_osumat/N:.2f} ')