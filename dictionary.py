class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        bello = path
        with open("resources/Italian.txt",'r') as file:
            for parola in file:
                self.dict.append(parola)
    def printAll(self):
        return self.dict.__str__()

    @property
    def dict(self):
        return self._dict