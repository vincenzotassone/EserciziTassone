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