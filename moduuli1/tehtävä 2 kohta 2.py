#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

import math
Sade = float(input("anna ympyrän säde"))
Pinta_ala = math.pi * Sade** 2
print("ympyrän pinta_ala on " + str(Pinta_ala))