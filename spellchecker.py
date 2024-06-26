import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multidic = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        testo = replaceChars(txtIn)
        t1 = time.time()
        self.multidic.searchWord(testo, language)
        tempo = f"time elapsed: {time.time()-t1}\n"
        stampa = self.multidic.paroleErrate+tempo
        t1 = time.time()
        stampa += "Metodo lineare \n"
        self.multidic.searchWordLinear(testo, language)
        tempo = f"time elapsed: {time.time() - t1}\n"
        stampa += self.multidic.paroleErrate + tempo
        t1 = time.time()
        stampa += "Metodo Dico \n"
        self.multidic.searchWordDichotomic(testo, language)
        tempo = f"time elapsed: {time.time() - t1}\n"
        stampa += self.multidic.paroleErrate + tempo
        return stampa

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text.lower()