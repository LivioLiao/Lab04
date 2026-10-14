
class Stand:
    def __init__(self, codice, metriQuadri, padiglione, prezzo_base):
        self.codice = codice
        self.metriQuadri = metriQuadri
        self.padiglione = padiglione
        self.prezzo_base = prezzo_base
        self.disponibile = True
        self.espositore = None

    def prezzo(self):
        return self.prezzo_base

    def __lt__(self,other):
        return self.prezzo() < other.prezzo()
    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore}"
        return (f"{self.codice}: Standard | {self.metriQuadri} mq - Padiglione "
                f"{self.padiglione} - Prezzo {self.prezzo():.2f}€ - {stato}")


class StandPrese(Stand):
    def __init__(self, codice, metriQuadri, padiglione, prezzo_base, prese):
        super().__init__(codice, metriQuadri, padiglione, prezzo_base)
        self.prese = prese

    def prezzo(self):
        return self.prezzo_base * (1 + 0.07*self.prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore}"
        return (f"{self.codice}: Prese Extra | {self.metriQuadri} mq - Padiglione "
                f"{self.padiglione} - Prezzo {self.prezzo():.2f}€ - Prese: {self.prese} - {stato}")


class StandPremium(Stand):
    def __init__(self, codice, metriQuadri, padiglione, prezzo_base, posizione):
        super().__init__(codice, metriQuadri, padiglione, prezzo_base)
        self.posizione = posizione

    def prezzo(self):
        return self.prezzo_base * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else f"Assegnato a {self.espositore}"
        return (f"{self.codice}: Premium | {self.metriQuadri} mq - Padiglione "
                f"{self.padiglione} - Prezzo {self.prezzo():.2f}€ - {self.posizione} - {stato}")


class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    def __str__(self):
        if self.stand is None:
            return f"{self.codice}: {self.nome} {self.cognome} - Nessuno stand"
        return f"{self.codice}: {self.nome} {self.cognome} - Stand: {self.stand}"







class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO

    def get_nome(self):
        return self.nome

    def set_nome(self,nome):
        self.nome = nome



    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try:
            file = open(file_path, "r")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")


        for riga in file:
            riga = riga.strip()
            if not riga:
                continue
            campo = riga.split(",")

            if len(campo) == 3:
                self.espositori.append(Espositore(campo[0], campo[1], campo[2]))

            elif len(campo) >= 4:
                codice = campo[0]
                mq = int(campo[1])
                pad = int(campo[2])
                prezzo = float(campo[3])

                if len(campo) == 4:
                    self.stand.append(Stand(codice, mq, pad, prezzo))
                else:
                    try:
                        n = int(campo[4])
                        self.stand.append(StandPrese(codice, mq, pad, prezzo, n))
                    except ValueError:
                        self.stand.append(StandPremium(codice, mq, pad, prezzo, campo[4]))







    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        stand = None
        for s in self.stand:
            if s.codice == codice_stand:
                stand = s
                break
        if stand is None:
            raise ValueError(f"Stand {codice_stand} inesistente")


        espositore = None
        for e in self.espositori:
            if e.codice == codice_espositore:
                espositore = e
                break
        if espositore is None:
            raise ValueError(f"Espositore {codice_espositore} inesistente")

        if not stand.disponibile:
            raise ValueError(f"Stand {codice_stand} non disponibile")
        if espositore.stand is not None:
            raise ValueError(f"Espositore {codice_espositore} già associato ad uno stand")

        stand.disponibile = False
        stand.espositore = espositore.codice
        espositore.stand = stand.codice





    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for e in self.espositori:
            print(e)


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stand)
