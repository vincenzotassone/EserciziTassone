def encrypt(text: str, key: int) -> str:
    risultato = ""

    for carattere in text:
        # Gestiamo le MAIUSCOLE (A-Z)
        if 'A' <= carattere <= 'Z':
            codice_ascii = ord(carattere)  # Esempio: 'A' -> 65
            norm = codice_ascii - 65  # Normalizza: 65-65 = 0
            nuovo = (norm + key) % 26  # Applica la formula
            risultato += chr(nuovo + 65)  # Torna a ASCII e aggiunge alla stringa

        # Gestiamo le MINUSCOLE (a-z)
        elif 'a' <= carattere <= 'z':
            codice_ascii = ord(carattere)  # Esempio: 'a' -> 97
            norm = codice_ascii - 97  # Normalizza: 97-97 = 0
            nuovo = (norm + key) % 26  # Applica la formula
            risultato += chr(nuovo + 97)  # Torna a ASCII e aggiunge alla stringa

        # Se non è una lettera (spazi, punti, numeri), non fare nulla
        else:
            risultato += carattere

    return risultato


def main():
    print("--- PROGRAMMA CIFRARIO DI CESARE ---")

    scelta = input("Vuoi cifrare (c) o decifrare (d)? ").lower()
    messaggio = input("Inserisci il testo: ")
    chiave = int(input("Inserisci la chiave (numero intero): "))

    if scelta == 'd':
        # Se l'utente vuole decifrare, passiamo la chiave negativa (-chiave)
        risultato_finale = encrypt(messaggio, -chiave)
    else:
        # Altrimenti usiamo la chiave normale
        risultato_finale = encrypt(messaggio, chiave)

    print(f"Risultato: {risultato_finale}")


# Questo pezzetto serve a far partire il programma quando premi "Play"
if __name__ == "__main__":
    main()