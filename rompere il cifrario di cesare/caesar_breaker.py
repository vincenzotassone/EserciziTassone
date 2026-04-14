def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:

            result += char
    return result


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    risultati = []

    for chiave in range(26):  
        testo_decifrato = encrypt(ciphertext, -chiave)
        risultati.append((chiave, testo_decifrato))

    return risultati