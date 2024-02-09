#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
#tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi
#kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin
#vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

season = ("winter", "winter", "spring", "spring", "spring", "summer",
          "summer", "summer", "autumn", "autumn", "autumn", "winter")
order = int(input("Give season (1-12): "))
month = season[order -1]

print(f"{order}. Month is {month}.")