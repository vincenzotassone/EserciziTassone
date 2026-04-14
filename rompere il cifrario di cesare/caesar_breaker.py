def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Controlla: è una lettera?
            # Capisce se deve partire dalla 'A' (65) o dalla 'a' (97)
            start = ord('A') if char.isupper() else ord('a')

            # La formula magica:
            # 1. Prende la lettera (ord)
            # 2. Sottrae l'inizio (0-25)
            # 3. Aggiunge lo spostamento
            # 4. Usa % 26 per ricominciare da capo se supera la 'Z'
            new_char = chr(start + (ord(char) - start + shift) % 26)
            result += new_char
        else:
            # Se è uno spazio o una virgola, lascialo così com'è
            result += char
    return result


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    risultati = []  # Qui salveremo tutte le prove

    for chiave in range(26):  # Prova i numeri da 0 a 25
        # Decifriamo usando la chiave negativa
        testo_decifrato = encrypt(ciphertext, -chiave)

        # Salviamo la coppia (chiave, testo) in una "tupla"
        # Una tupla è come una scatola chiusa con due valori: (5, "Hello")
        risultati.append((chiave, testo_decifrato))

    return risultati  # Restituisce tutta la lista di prove