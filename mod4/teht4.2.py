#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes
#käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

while True:
    tuumat = float(input("Montako tuumaa?"))
    print((tuumat * 2.54), "cm")
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break








