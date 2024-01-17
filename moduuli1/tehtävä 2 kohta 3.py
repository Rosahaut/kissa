#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = float(input("anna suorakulmion kanta"))
korkeus = float(input("anna suorakulman korkeus"))
piiri = kanta * 2 + korkeus * 2
pinta_ala = kanta * korkeus
print("suorakulmion piiri ja pinta_ala on" + str(piiri) + " " + str(pinta_ala))
