#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiv = float(input("anna massa leivisköinä "))
naula = float(input("anna massa nauloina "))
luoti = float(input("anna massa luoteina "))
naulojen_summat = leiv * 20 + naula
luotien_summa = naulojen_summat * 32 + luoti
grammat = luotien_summa * 13.3
kg = int(grammat / 1000)
g = int(grammat % 1000)
print("tulos: " + str(kg) + "kg " + str(g) + "g")