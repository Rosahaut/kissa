#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).

oikea_tunnus = "python"
oikea_salasana = "rules"

yrityskerta = 5

while yrityskerta > 0:
    tunnus = input("Syötä käyttäjätunnus: ")
    salasana = input("Syötä salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break
    else:
        print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
        yrityskerta -= 1

if yrityskerta == 0:
    print("Game over. kaikki yrityskerrat on käytetty.")
