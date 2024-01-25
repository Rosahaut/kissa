#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha_pituus = float(input("Anna kuhan pituus senttimetreinä: "))

alamitta_raja = 37

if kuha_pituus < alamitta_raja:
    alimman_mitan_puute = alamitta_raja - kuha_pituus
    print(f"Kuha on alamittainen! Laske se takaisin järveen. Puuttuu {alimman_mitan_puute} cm alimmasta sallitusta pyyntimitasta.")
else:
    print("Kuha on sallitun mittainen. saat pitää!.")




