

leiviska2 = float(input("Anna leiviskät:"))
naula2 = float(input("Anna naulat:"))
luoti2 = float(input("Anna luodit:"))


leiviska = naula2 * leiviska2
naula = naula2 * luoti2
luoti = 0.0133 * luoti2


massa = leiviska + luoti + naula
print("Massa nykymittojen mukaan:", massa),print("kg")
