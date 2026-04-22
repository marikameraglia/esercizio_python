class Studente:
    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = []

    def presentati(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}."

    def aggiungi_voto(self, voto):
        if 18 <= voto <= 30:
            self.voti.append(voto)
            print(f"Voto {voto} aggiunto a {self.nome}.")
        else:
            print("Voto non valido (deve essere tra 18 e 30).")

    def calcola_media(self):
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def studia(self, ore):
        print(f"{self.nome} sta studiando da {ore} ore per l'esame!")


# --- ESECUZIONE DEL PROGRAMMA ---

# 1. Creazione di due oggetti (istanze) della classe Studente
studente1 = Studente("Marika", "Meraglia", 22, "12345")
studente2 = Studente("Luca", "Rossi", 24, "67890")

# 2. Utilizzo dei metodi per lo Studente 1
print(studente1.presentati())
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)
studente1.studia(4)
print(f"Media voti di {studente1.nome}: {studente1.calcola_media():.2f}")

print("-" * 30)

# 3. Utilizzo dei metodi per lo Studente 2
print(studente2.presentati())
studente2.aggiungi_voto(24)
studente2.aggiungi_voto(26)
studente2.studia(2)
print(f"Media voti di {studente2.nome}: {studente2.calcola_media():.2f}")
