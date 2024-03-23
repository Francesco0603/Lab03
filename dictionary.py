class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self, path):
        if not isinstance(path, str):
            raise ValueError("Il percorso deve essere una stringa")
        try:
            with open(f"resources/{path}", 'r', encoding='utf-8') as file:
                for parola in file:
                    self.dict.append(parola)  # Aggiunge le parole al dizionario
        except FileNotFoundError:
            raise FileNotFoundError(f"Il file {path} non è stato trovato")

    def printAll(self):
        return self.dict.__str__()

    @property
    def dict(self):
        return self._dict