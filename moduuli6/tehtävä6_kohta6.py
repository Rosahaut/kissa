#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
#sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan euroina
#per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä
#ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi
#yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

def laske_yksikkohinta(halkaisija, hinta):
    pinta_ala = 3.1416 * (halkaisija / 2) ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

# Pääohjelma
halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
hinta1 = float(input("Syötä ensimmäisen pizzan hinta (euroa): "))

halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
hinta2 = float(input("Syötä toisen pizzan hinta (euroa): "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta1 > yksikkohinta2:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat ovat samanhintaisia neliömetriä kohden.")

