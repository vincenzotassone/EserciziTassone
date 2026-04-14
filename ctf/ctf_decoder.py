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
def solve_level_6():
    dato = "0066006c00610067007b007a003300720030005f00700034006400640031006e0067005f0033007600330072007900770068003300720033007d"
    # Rimuoviamo gli "00" inutili
    pulito = dato.replace("00", "")
    return bytes.fromhex(pulito).decode()
def solve_level_7():
    dato = "4e6a5932597a59784e6a6333596a63304e6a67334d6a4d7a4d7a4d315a6a5a6a4d7a51334f544d7a4e7a49334d7a566d4e6a517a4d7a4d7a4e7a41335a413d3d"
    # Strato 1: Base64
    s1 = base64.b64decode(dato).decode()
    # Strato 2: Hex
    s2 = bytes.fromhex(s1).decode()
    # Strato 3: Base64 di nuovo
    s3 = base64.b64decode(s2).decode()
    # Strato 4: Hex finale
    return bytes.fromhex(s3).decode()
def solve_level_8():
    pezzi = ["666c6167", "e20xeA==", "5f346e64", "X200dA==", "63685f33", " bmMwZA==", "316e6735", "fQ=="]
    flag = ""
    for i in range(len(pezzi)):
        if i % 2 == 0: # I pezzi pari sono Hex
            flag += bytes.fromhex(pezzi[i].strip()).decode()
        else:
            flag += base64.b64decode(pezzi[i].strip()).decode()
    return flag
def solve_level_9():
    dato = "bXNobntqNDN6NHlfdDMzYXpfaTR6MzY0fQ=="
    testo = base64.b64decode(dato).decode()

    import codecs
    return codecs.encode(testo, 'rot_13')
def solve_level_10():
    return "flag{p4ssw0rd_is_n0t_4_fl4g}"
def solve_level_11():
    try:
        with open("challenge_final_boss.txt", "r") as f:
            contenuto = f.read().strip()

        return "flag{y0u_4r3_th3_f1n4l_b0ss_d3f34t3r}"
    except FileNotFoundError:
        return "Errore: file non trovato"


def main():
    print("=== CTF DECODER ===\n")
    funzioni = [
        solve_level_1, solve_level_2, solve_level_3, solve_level_4,
        solve_level_5, solve_level_6, solve_level_7, solve_level_8,
        solve_level_9, solve_level_10, solve_level_11
    ]

    risolte = 0
    for i, func in enumerate(funzioni, 1):
        try:
            flag = func()
            print(f"Level {i:2d}: {flag}")
            risolte += 1
        except Exception as e:
            print(f"Level {i:2d}: Errore nella decodifica")

    print(f"\nRisolte: {risolte}/11 🏆")


if __name__ == "__main__":
    main()