#Kirjoita ohjelma, joka kysyy käyttäjän biologisen
#sukupuolen ja hemoglobiiniarvon (g/l). Ohjelma ilmoittaa,
#onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
sukupuoli = input("Oletko mies vai nainen? ")
hemo = float(input("Mikä on sinun hemoglobiiniarvo? "))
if sukupuoli == "mies" and hemo>=134 and hemo <=195:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli =="mies" and hemo<134:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli =="mies" and hemo >195:
    print("Hemoglobiiniarvosi on korkea.")

if sukupuoli == "nainen" and hemo >=117 and hemo <=175:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli =="nainen" and hemo<117:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli =="nainen" and hemo>175:
    print("Hemoglobiiniarvosi on korkea.")


















