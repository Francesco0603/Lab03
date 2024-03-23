import spellchecker

sc = spellchecker.SpellChecker()
flag = False
while(True):
    sc.printMenu()

    # versione quasi finita 23/03
    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        stampaContains = sc.handleSentence(txtIn,"italian")
        print("Metodo Contains, che in realtà ho usato un in...")
        print(stampaContains)
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        stampaContains = sc.handleSentence(txtIn,"english")
        print("Metodo Contains, che in realtà ho usato un in...")
        print(stampaContains)
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        stampaContains = sc.handleSentence(txtIn,"spanish")
        print("Metodo Contains, che in realtà ho usato un in...")
        print(stampaContains)
        continue

    if int(txtIn) == 4:
        break


