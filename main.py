import sqlite3

# 1. Connessione al database (crea il file se non esiste)
conn = sqlite3.connect("esercitazione.db")
cursor = conn.cursor()

# 2. Creazione della tabella 'contatti'
# IF NOT EXISTS evita errori se la tabella c'è già
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS contatti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        tel TEXT NOT NULL
    )
"""
)

print("\n--- DATABASE PRONTO ---")

# 3. Richiesta dati all'utente
nome = input("Inserisci un nome: ")
telefono = input("Inserisci un numero: ")

# 4. Inserimento dei dati nel database
# Usiamo i '?' per sicurezza (evita SQL Injection)
cursor.execute("INSERT INTO contatti (nome, tel) VALUES (?, ?)", (nome, telefono))

# 5. Salva le modifiche e chiudi la connessione
conn.commit()
conn.close()

print("\nDati salvati con successo!")
input("Premi INVIO per uscire...")
