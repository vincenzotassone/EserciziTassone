import base64
def solve_level_1():
    h = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    # Trasforma i numeri esadecimali in testo leggibile
    return bytes.fromhex(h).decode()

def solve_level_2():
    p1_b64 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
    p1 = base64.b64decode(p1_b64).decode()
    p2_int = 664813035583918006462745898431981286737635929725
    lunghezza = (p2_int.bit_length() + 7) // 8
    p2 = p2_int.to_bytes(lunghezza, 'big').decode()

    return p1 + p2

def solve_level_3():
    dato = "NjY2YzYxNjc3YjZjMzQ3OTMzNzIzNTVmMzA2ZTVmNmMzNDc5MzM3MjM1N2Q="
    # Prima togliamo il Base64, otteniamo una stringa esadecimale
    hex_str = base64.b64decode(dato).decode()
    # Poi trasformiamo l'esadecimale in testo
    return bytes.fromhex(hex_str).decode()

def solve_level_4():
    dato = "Wm14aFozdGlOSE16WDNNeGVIUjVYMll3ZFhKZk1XNWpNM0IwTVRCdWZRPT0="
    # Bisogna decodificare 3 volte!
    passo1 = base64.b64decode(dato)
    passo2 = base64.b64decode(passo1)
    flag = base64.b64decode(passo2).decode()
    return flag
def solve_level_5():
    dato = "7d72337474346d5f73337479625f35647234776b6334627b67616c66"
    # Inverto la stringa usando [::-1]
    dato_dritto = dato[::-1]
    # Ora che è dritta, decodifico l'esadecimale
    return bytes.fromhex(dato_dritto).decode()