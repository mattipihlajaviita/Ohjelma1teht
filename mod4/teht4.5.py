"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen
ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
tunnus ja salasana kysytään uudelleen. Tätä jatketaan
kunnes kirjautumistiedot ovat oikein tai väärät tiedot
on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan
Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules)
"""
#käyttäjätunnus ja salasana
username = "python"
password = "rules"

#annetaan muuttujille arvot
yritykset = 0
yritykset_max = 5

#pyydetään käyttäjää syöttämään tunnus ja salasana
username_input = input("Syötä käyttäjätunnus: ")
password_input = input("Syötä salasana: ")

#tehdään silmukka, joka päättyy kun käyttäjä syöttää oikeat tiedot
#tai kun käyttäjä syöttää väärät tiedot 5 kertaa
while username != username_input or password != password_input:
    print("Väärä käyttäjänimi ja/tai salasana, yritä uudelleen")

    #lisätään yritys ja pyydetään käyttäjää syöttämään tiedot uudelleen
    yritykset = yritykset + 1
    username_input = input("Syötä käyttäjätunnus: ")
    password_input = input("Syötä salasana: ")

    #jos yrityksiä 5, evätään käyttäjältä pääsy, ohjelma sammuu
    if yritykset == yritykset_max:
        print("Pääsy evätty.")
        break

#käyttäjä pääsee sisään
else:
    print("Tervetuloa!")




