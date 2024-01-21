def tulosta_hytin_kuvaus(hyttiluokka):
    if hyttiluokka == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
    elif hyttiluokka == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif hyttiluokka == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif hyttiluokka == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print("Virheellinen hyttiluokka.")

def main():
    hyttiluokka = input("Syötä laivan hyttiluokka (LUX, A, B, C): ").upper()
    tulosta_hytin_kuvaus(hyttiluokka)

if __name__ == "__main__":
    main()
