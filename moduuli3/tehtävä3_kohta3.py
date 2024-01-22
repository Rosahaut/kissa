def tarkista_hemoglobiini(sukupuoli, hemoglobiiniarvo):
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
        print("Virheellinen syöte sukupuoleen. Käytä 'nainen' tai 'mies'.")

def main():
    try:
        sukupuoli = input("Syötä sukupuoli (nainen/mies): ")
        hemoglobiiniarvo = float(input("Syötä hemoglobiiniarvo (g/l): "))
        tarkista_hemoglobiini(sukupuoli, hemoglobiiniarvo)
    except ValueError:
        print("Virheellinen syöte hemoglobiiniarvoon. Syötä numeroarvo.")

if __name__ == "__main__":
    main()

