import dictionary as d
import richWord as rw
import math as math


class MultiDictionary:

    def __init__(self):
        self.dictionary = d.Dictionary()
        self._richWords = []

    def selezionaLingua(self,language):
        if language.__eq__("english"):
            self.dictionary.loadDictionary('English.txt')
        if language.__eq__("italian"):
            self.dictionary.loadDictionary("Italian.txt")
        if language == "spanish":
            self.dictionary.loadDictionary('Spanish.txt')
    def printDic(self, language):
        self.selezionaLingua(language)
        self.dictionary.printAll()

    def searchWord(self, words, language):
        self._richWords.clear()
        self.selezionaLingua(language)
        wordsList = words.split(" ")
        for inputWord in wordsList:
            parolinaMagica = inputWord+"\n"
            rword = rw.RichWord(parolinaMagica)
            if parolinaMagica in self.dictionary.dict:
                rword.setCorretta(True)
            else:
                rword.setCorretta(False)
                self._richWords.append(parolinaMagica)
    def searchWordLinear(self, words, language):
        self._richWords.clear()
        self.selezionaLingua(language)
        wordsList = words.split(" ")
        for inputWord in wordsList:
            flag = True
            parolinaMagica = inputWord + "\n"
            rword = rw.RichWord(parolinaMagica)
            for dicWord in self.dictionary.dict:
                if dicWord == inputWord:
                    rword.setCorretta(True)
                    flag = False
                    break
            if flag:
                rword.setCorretta(False)
                self._richWords.append(parolinaMagica)
    def searchWordDichotomic(self, words, language):
        self._richWords.clear()
        self.selezionaLingua(language)
        wordsList = words.split(" ")
        for inputWord in wordsList:
            parolinaMagica = inputWord + "\n"
            rword = rw.RichWord(parolinaMagica)
            lunghezzaDict = len(self.dictionary.dict)
            newDic = self.dictionary.dict
            for n in range(round(math.log(lunghezzaDict,2))):
                if parolinaMagica == newDic[(lunghezzaDict)/2]:
                    rword.setCorretta(True)
                    flag = False
                    break
                elif parolinaMagica < newDic[(lunghezzaDict)/2]:
                    newDic = newDic[((lunghezzaDict)/2):]
                else:
                    newDic = newDic[:((lunghezzaDict)/2)]
            if flag:
                rword.setCorretta(False)
                self._richWords.append(parolinaMagica)

    @property
    def paroleErrate(self):
        stampa = ""
        for parola in self._richWords:
            stampa += parola
        return stampa


