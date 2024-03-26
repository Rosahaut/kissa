# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
# joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka
# (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Release:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print("Release name:", self.name)


class Book(Release):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        super().print_info()
        print("Author:", self.author)
        print("Page count:", self.page_count)


class Magazine(Release):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        super().print_info()
        print("Editor:", self.editor)


aku_ankka = Magazine("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Book("Hytti n:o 6", "Rosa Liksom", 200)

print("\nMagazine:")
aku_ankka.print_info()
print("\nBook:")
hytti_no_6.print_info()
