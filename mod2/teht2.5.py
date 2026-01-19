#1 leiviskä = 20 naulaa
#1 naula = 32 luotia
#1 1 luoti = 13.3 grammaa
leiviska = float(input("Anna leiviskät:"))
naula = float(input("Anna naulat:"))
luoti = float(input("Anna luodit:"))

luotipaino1 = 0.0133
naulapaino1 = luotipaino1 * 32
leiviskapaino1 = naulapaino1 * 20

massa = (luoti * luotipaino1) + (naulapaino1 * naula) + (leiviska * leiviskapaino1)

kilot = int(massa)
grammat = round((massa - kilot) * 1000)
print("Massa nykymittojen mukaan:")
print(kilot,"kilogrammaa ja",grammat,"grammaa")









