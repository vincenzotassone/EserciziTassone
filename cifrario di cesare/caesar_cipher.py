def encrypt(text: str, key: int) -> str:
    risultato = ""

    for carattere in text:
        if 'A' <= carattere <= 'Z':
            codice_ascii = ord(carattere)
            norm = codice_ascii - 65
            nuovo = (norm + key) % 26
            risultato += chr(nuovo + 65)
        elif 'a' <= carattere <= 'z':
            codice_ascii = ord(carattere)
            norm = codice_ascii - 97
            nuovo = (norm + key) % 26
            risultato += chr(nuovo + 97)
        else:
            risultato += carattere

    return risultato


def main():
    print("--- PROGRAMMA CIFRARIO DI CESARE ---")

    scelta = input("Vuoi cifrare (c) o decifrare (d)? ").lower()
    messaggio = input("Inserisci il testo: ")
    chiave = int(input("Inserisci la chiave (numero intero): "))

    if scelta == 'd':
        risultato_finale = encrypt(messaggio, -chiave)
    else:
        risultato_finale = encrypt(messaggio, chiave)
    print(f"Risultato: {risultato_finale}")

if __name__ == "__main__":
    main()