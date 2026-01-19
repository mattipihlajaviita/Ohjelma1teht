#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan
#(LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen
#alla olevan luettelon mukaisesti. Tehtävässä on käytettävä
#if/elif/else-toistorakennetta.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.
#Jos käyttäjä syöttää kelvottoman hyttiluokan,
#ohjelma tulostaa Virheellinen hyttiluokka.

luokka = input("Kerro hyttiluokkasi: ")
if luokka.lower() == "lux":
    print("Teille on parvekkeellinen hytti yläkannella.")
elif luokka.lower() == "a":
    print ("Teille on ikkunallinen hytti autokannen yläpuolella.")
elif luokka.lower() == "b":
    print("Teille on ikkunaton hytti autokannen yläpuolella")
elif luokka.lower() == "c":
    print("Teille on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hyttiluokka")


