#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
#Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
#Kuha on alamittainen, jos sen pituus on alle 37 cm.

def tarkista_kuha_pituus():
    alaraja = 37

    try:
        kuhan_pituus = float(input("Syötä kuhan pituus senttimetreinä: "))
        if kuhan_pituus < alaraja:
            puuttuvat_sentit = alaraja - kuhan_pituus
            print(f"Kuha on alamittainen. Laske se takaisin järveen. Puuttuvat sentit: {puuttuvat_sentit} cm.")
        else:
            print("Kuha on sallitun mittainen. Voit pitää sen.")
    except ValueError:
        print("Virheellinen syöte. Syötä kuhan pituus numeroina.")

if __name__ == "__main__":
    tarkista_kuha_pituus()



