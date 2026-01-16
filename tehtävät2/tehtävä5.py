#1 leiviskä = 20 naulaa
#1 naula = 32 luotia
#1 1 luoti = 13.3 grammaa
leiviska = int(input("Anna leiviskät:"))
naula = int(input("Anna naulat:"))
luoti = int(input("Anna luodit:"))

luotipaino1 = 13.3
naulapaino1 = luotipaino1 * 32
leiviskapaino1 = naulapaino1 * 20

massa = (luoti * luotipaino1) + (naulapaino1 * naula) + (leiviska * leiviskapaino1)
print("Massa nykymittojen mukaan on:", massa,"grammaa" )









