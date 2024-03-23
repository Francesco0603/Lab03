import spellchecker

sc = spellchecker.SpellChecker()
flag = False
while(True):
    sc.printMenu()

    if flag:
        print("------------------------\n")
        print("Metodo Contains, che in realtà ho usato un in...\n")
        print(stampaContains)
        print("------------------------\n")

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        stampaContains = sc.handleSentence(txtIn,"italian")
        flag = True
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        stampaContains = sc.handleSentence(txtIn,"english")
        flag = True
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        stampaContains = sc.handleSentence(txtIn,"spanish")
        flag = True
        continue

    if int(txtIn) == 4:
        break


