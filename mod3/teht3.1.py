#Kirjoita ohjelma, joka kysyy kalastajalta
#kuhan pituuden senttimetreinä. Jos kuha on alamittainen,
#ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla
#käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhan_pituus = float(input("Kalastamasi kuhan pituus senttimetreinä: "))
alimitta = 37 - kuhan_pituus
if kuhan_pituus < 37:
    print ("Laske kuha takaisin järveen, kuha on", alimitta, "cm liian pieni")
if kuhan_pituus >= 37:
    print("Voit heittää kuhan pannulle.")
