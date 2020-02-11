def podziel_do_dlugosci(bity_wyslane, dlugosc_wyslana):
    def _f(bity, dlugosc):
        while bity:
            if len(bity) < dlugosc:
                x = bity.ljust(dlugosc, '0')
                bity = x
            yield bity[:dlugosc]
            bity = bity[dlugosc:]

    return list(_f(bity_wyslane, dlugosc_wyslana))
