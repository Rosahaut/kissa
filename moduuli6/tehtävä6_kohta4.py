#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
#Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
#jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def calculate_sum(number_list):
    return sum(number_list)


def main():
    test_list = [1, 2, 3, 4, 5]

    total_sum = calculate_sum(test_list)
    print(f"total sum on list: {total_sum}")

if __name__ == "__main__":
    main()
