#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = int(input("anna ensimmäinen kokonaisluku"))
luku2 = int(input("anna toinen kokonaisluku"))
luku3 = int(input("anna kolmas kokonaisluku"))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3
print("kokonaisluvun summa" + str(summa))
print("kokonaisluvun tulo" + str(tulo))
print("kokonaisluvun keskiarvo" + str(keskiarvo))

