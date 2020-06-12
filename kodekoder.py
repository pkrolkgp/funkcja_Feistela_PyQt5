from okno_aplikacji import OknoGeneratora as Generator
class Kodekoder:
    tabela_transkrypcji = {
        "11110": "",
        "A": "110",
        "a": "120",
        "Ą": "130",
        "ą": "140",
        "B": "150",
        "b": "160",
        "C": "170",
        "c": "180",
        "Ć": "190",
        "ć": "210",
        "D": "220",
        "d": "230",
        "E": "240",
        "e": "250",
        "Ę": "260",
        "ę": "270",
        "F": "280",
        "f": "290",
        "G": "310",
        "g": "320",
        "H": "330",
        "h": "340",
        "I": "350",
        "i": "360",
        "J": "370",
        "j": "380",
        "K": "390",
        "k": "410",
        "L": "420",
        "l": "430",
        "Ł": "440",
        "ł": "450",
        "M": "460",
        "m": "470",
        "N": "480",
        "n": "490",
        "Ń": "510",
        "ń": "520",
        "O": "530",
        "o": "540",
        "Ó": "550",
        "ó": "560",
        "P": "570",
        "p": "580",
        "R": "590",
        "r": "610",
        "S": "620",
        "s": "630",
        "Ś": "640",
        "ś": "650",
        "T": "660",
        "t": "670",
        "U": "680",
        "u": "690",
        "W": "710",
        "w": "720",
        "Y": "730",
        "y": "740",
        "Z": "750",
        "z": "760",
        "Ź": "770",
        "ź": "780",
        "Ż": "790",
        "ż": "810",
        ".": "820",
        ",": "830",
        "!": "840",
        "?": "850",
        "(": "860",
        ")": "870",
        ";": "880",
        ":": "890",
        "\n": "980",
        " ": "990",
        "–": "910",
        "-": "920",
        "\"": "930",
        "„": "940",
        "”": "950",
        "@": "960",
        "%": "970",
        # "q": "1110",
        # "Q": "1110",
        # "v": "1110",
        # "V": "1110",
        # "x": "1110",
        # "X": "1120"
    }

    def tekst_na_liczby(self, tekst):
        return self.tabela_transkrypcji.get(tekst)

    def liczby_na_tekst(self, liczba):
        listaKluczy = list()
        listaWartosci = self.tabela_transkrypcji.items()
        for litera in listaWartosci:
            if litera[1] == liczba:
                listaKluczy.append(litera[0])
        return listaKluczy

    def szyfrowanie(self, tekst_do_szyfrowania):
        zaszyfrowany = ""
        aktualna_litera = ""
        try:
            for litera in tekst_do_szyfrowania:
                aktualna_litera = litera
                zaszyfrowany += self.tekst_na_liczby(litera)
            return zaszyfrowany
        except:
            Generator.blad_pokaz("Błąd szyfrowania, niedozwolony znak: " + aktualna_litera)

    def deszyfrowanie(self, tekst_do_odszyfrowania):
        odszyrowany = ""
        ciag = ""
        try:
            for liczba in tekst_do_odszyfrowania:
                if liczba != "0":
                    ciag += liczba
                else:
                    odszyrowany += "".join(self.liczby_na_tekst(ciag + "0"))
                    ciag = ""
            return odszyrowany
        except:
            Generator.blad_pokaz("Błąd Odszyfrowania")
