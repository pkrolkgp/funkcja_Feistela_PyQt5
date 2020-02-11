def tekst_do_bitow(tekst):
    return ''.join([bin(ord(x))[2:].zfill(16) for x in tekst])


def bity_do_tekstu(bity):
    string = ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(bity)] * 16))
    return string
