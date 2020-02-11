def mapowanie_procentow(wartosc, lewa_min, lewa_max, prawa_min, prawa_max):
    lewa = lewa_max - lewa_min
    prawa = prawa_max - prawa_min
    wartosc_przeskalowana = float(wartosc - lewa_min) / float(lewa)
    return prawa_min + (wartosc_przeskalowana * prawa)

