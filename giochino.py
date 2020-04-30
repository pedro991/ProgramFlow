import random

ex_list = []
highest = 77
solution = random.randint(1, highest)

print("""Oh no! Un bug ha maledetto un numero casuale tra 1 e {} :(
L'unico modo di trovarlo è andare per esclusione:
    inserendo un valore maggiore del numero maledetto, escluderai tutti quelli al di sopra.0
    Inserendo invece un valore minore del numero maledetto, escluderai tutti quelli al di sotto.
    Inserisci il numero maledetto e..  ¯\_(ツ)_/¯ """.format(highest))
guess = int(input())

while guess != 0:
    if guess == solution:
        print("Oh noo, hai perso! ;( \n Il numero era proprio {}".format(solution))
        break
    elif guess in ex_list:
        print("Ma sei scemo? Vedi che è una cosa importante...")
        guess = int(input())
    elif guess < solution:
        for k in range(0, guess+1):
            if k not in ex_list:
                ex_list.append(k)
        if len(ex_list) == 100:
            print("Hurra! Hai vinto!! (☞ﾟヮﾟ)☞ \nIl numero era {}!".format(solution))
            break
        line = ""
        for i in range(1, 101):
            if i in ex_list:
                line += "|{:3}".format(" ")
            else:
                line += "|{:3}".format(i)
            if i % 10 == 0:
                print(line+"|")
                line = ""
        guess = int(input())
    elif guess > solution:
        for k in range(guess, 101):
            if k not in ex_list:
                ex_list.append(k)
        if len(ex_list) == 100:
            print("Hurra! Hai vinto!! (☞ﾟヮﾟ)☞\nIl numero era {}!".format(solution))
            break
        line = ""
        for i in range(1, 101):
            if i in ex_list:
                line += "|{:3}".format(" ")
            else:
                line += "|{:3}".format(i)
            if i % 10 == 0:
                print(line+"|")
                line = ""
        guess = int(input())
