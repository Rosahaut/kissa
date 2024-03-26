import numpy as np

#tehtävä 1 kohta 1
rad_a = 2.493
rad_b = 0.911

asteet_a = np.degrees(rad_a)
asteet_b = np.degrees(rad_b)

print("a) 2.493 rad on", asteet_a, "astetta.")
print("b) 0.911 rad on", asteet_b, "astetta.\n")

#tehtävä 1 kohta 2
asteet_a = 137.7
asteet_b = 62.3

rad_a = np.radians(asteet_a)
rad_b = np.radians(asteet_b)

print("a) 137.7 astetta on", rad_a, "radiaania.")
print("b) 62.3 astetta on", rad_b, "radiaania.\n")

#tehtävä 1 kohta 3
import numpy as np

kulmat_astetta = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]

kulmat_radiaaneina = np.radians(kulmat_astetta)

print("Kulmat radiaaneina:")
for kulma_rad in kulmat_radiaaneina:
    print(kulma_rad)

#tehtävä 2
kateetti1 = 1.6  # metriä
kateetti2 = 2.3  # metriä

hypotenuusa = np.sqrt(np.square(kateetti1) + np.square(kateetti2))

print("\nSuorakulmaisen kolmion hypotenuusa on:", hypotenuusa, "metriä.")



