#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Syötä biologinen sukupuoli (Nainen/Mies): ")

hemoglobiiniarvo = float(input("Syötä hemoglobiiniarvo (g/l): "))

if sukupuoli.lower() == "nainen":
    if 117 <= hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli.lower() == "mies":
    if 134 <= hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    elif hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")

