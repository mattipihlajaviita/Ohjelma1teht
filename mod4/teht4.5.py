#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen
#ja salasanan. Jos jompikumpi tai molemmat ovat väärin,
#tunnus ja salasana kysytään uudelleen. Tätä jatketaan
#kunnes kirjautumistiedot ovat oikein tai väärät tiedot
#on syötetty viisi kertaa. Edellisessä tapauksessa tulostetaan
#Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules)
username = "python"
password = "rules"

yritykset = 0
yritykset_max = 5

username_input = input("Syötä käyttäjätunnus: ")
password_input = input("salasana: ")

while username != username_input or password != password_input:
    print("Väärä käyttäjänimi ja/tai salasana, yritä uudelleen")
    yritykset = yritykset + 1
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("salasana: ")
    if yritykset >= yritykset_max:
        print("Pääsy evätty.")
        break

else:
    print("Tervetuloa!")




