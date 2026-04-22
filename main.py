class Studente:
    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []

    def presentati(self):
        return f"Studente: {self.nome} {self.cognome} | Età: {self.eta} | Matricola: {self.matricola}"

    def aggiungi_voto(self, voto):
        if 18 <= voto <= 30:
            self.voti.append(voto)
        else:
            print(f"Attenzione: Il voto {voto} non è valido!")

    def calcola_media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        print(f"L'alunno {self.nome} {self.cognome} ha studiato per {ore} ore.")


# --- DIMOSTRAZIONE FUNZIONAMENTO ---

print("=" * 40)
print("  ESERCITAZIONE FINALE: CLASSE STUDENTE  ")
print("=" * 40)

# Creazione degli oggetti
studente1 = Studente("Marika", "Meraglia", 22, "M12345")
studente2 = Studente("Luca", "Rossi", 24, "L67890")

# Azioni Studente 1
print(f"\n[TEST 1] {studente1.presentati()}")
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)
studente1.studia(5)
print(f"Media voti: {studente1.calcola_media():.2f}")

print("-" * 20)

# Azioni Studente 2
print(f"[TEST 2] {studente2.presentati()}")
studente2.aggiungi_voto(24)
studente2.aggiungi_voto(26)
studente2.studia(3)
print(f"Media voti: {studente2.calcola_media():.2f}")

print("\n" + "=" * 40)
print("       ESECUZIONE COMPLETATA          ")
print("=" * 40)
