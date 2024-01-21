def on_karkausvuosi(vuosi):
    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        vuosi = int(input("Syötä vuosiluku: "))
        if on_karkausvuosi(vuosi):
            print(f"{vuosi} on karkausvuosi.")
        else:
            print(f"{vuosi} ei ole karkausvuosi.")
    except ValueError:
        print("Virheellinen syöte. Syötä vuosiluku kokonaislukuna.")

if __name__ == "__main__":
    main()
