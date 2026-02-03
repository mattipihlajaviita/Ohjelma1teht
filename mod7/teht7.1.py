"""Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia
vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
että joulukuu on ensimmäinen talvikuukausi."""

talvikuukaudet = (12,1,2)
kevätkuukaudet = (3,4,5)
kesäkuukaudet = (6,7,8)
syyskuukaudet = (9,10,11)

numero = int(input("Anna kuukauden numero: "))
if numero in talvikuukaudet:
    print("Talvi")
elif numero in kevätkuukaudet:
    print("Kevät")
elif numero in kesäkuukaudet:
    print("Kesä")
elif numero in syyskuukaudet:
    print("Syksy")









