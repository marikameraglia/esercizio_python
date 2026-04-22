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
            print(f"Attenzione: Il voto {voto} per {self.nome} non è valido!")

    def calcola_media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        print(f"L'alunno {self.nome} {self.cognome} ha studiato per {ore} ore.")


# --- DIMOSTRAZIONE FUNZIONAMENTO CON 5 STUDENTI ---

print("=" * 50)
print("   ESERCITAZIONE FINALE: GESTIONE CLASSE STUDENTE   ")
print("=" * 50)

# 1. Creazione dei 5 oggetti (Istanze)
s1 = Studente("Marika", "Meraglia", 22, "M12345")
s2 = Studente("Luca", "Rossi", 24, "L67890")
s3 = Studente("Giulia", "Bianchi", 21, "B11223")
s4 = Studente("Marco", "Verdi", 23, "V44556")
s5 = Studente("Sofia", "Neri", 22, "N77889")

# Lista per automatizzare la stampa
studenti = [s1, s2, s3, s4, s5]

# Assegnazione voti e ore di studio casuali per il test
s1.aggiungi_voto(28)
s1.aggiungi_voto(30)
s1.studia(5)
s2.aggiungi_voto(24)
s2.aggiungi_voto(26)
s2.studia(3)
s3.aggiungi_voto(30)
s3.aggiungi_voto(29)
s3.studia(6)
s4.aggiungi_voto(18)
s4.aggiungi_voto(22)
s4.studia(2)
s5.aggiungi_voto(27)
s5.aggiungi_voto(25)
s5.studia(4)

# 2. Visualizzazione Risultati
for i, studente in enumerate(studenti, 1):
    print(f"\n[TEST {i}] {studente.presentati()}")
    print(f"Media voti attuale: {studente.calcola_media():.2f}")
    print("-" * 30)

print("\n" + "=" * 50)
print("            ESECUZIONE COMPLETATA              ")
print("=" * 50)
