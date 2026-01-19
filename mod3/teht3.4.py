#Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa,
#onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi,
#jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia
#vain jos ne ovat jaollisia myös neljälläsadalla.

#Onko annettu vuosi karkausvuosi
#Jos vuosi on jaollinen 400:lla -> ON KARKAUSVUOSI
#Muuten jos vuosi on jaollinen 100:lla -> EI OLE KARKAUSVUOSI
#MUUTEN jos vuosi on jaollinen 4:lla - > ON KARKAUSVUOSI
#MUUTEN -> ei ole karkausvuosi

vuosi = int(input("Mikä vuosi? "))
if vuosi % 400 == 0 or vuosi % 4 == 0 and not vuosi % 100 == 0:
    print("Vuosi on karkausvuosi")
else:
  print("Vuosi ei ole karkausvuosi")


