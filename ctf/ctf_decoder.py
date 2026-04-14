import base64
def solve_level_1():
    h = "666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d"
    # Trasforma i numeri esadecimali in testo leggibile
    return bytes.fromhex(h).decode()