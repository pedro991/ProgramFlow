import random

ex_list = []
user_value = int(input("Inserisci un numero e il sistema lo arrotonderà al multiplo di 10 più vicino!"))
highest = int(round(user_value / 10, 0) * 10)
solution = random.randint(1, highest)

print("""Oh no! Un bug ha maledetto un numero casuale tra 1 e {} :(
L'unico modo di isolarlo è andare per esclusione:
    inserendo un valore maggiore del numero maledetto, escluderai tutti quelli al di sopra.
    Inserendo invece un valore minore del numero maledetto, escluderai tutti quelli al di sotto.
    Inserisci il numero maledetto e..  ¯\_(ツ)_/¯ """.format(highest))
guess = int(input())

while guess != 0:
    if guess == solution:
        print("Oh noo, hai perso! ;( \n Il numero era proprio {}".format(solution))
        break
    elif guess in ex_list or guess > highest:
        print("Ma sei scemo? Vedi che è una cosa importante...\nRiprova!")
        guess = int(input())
    elif guess < solution:
        for k in range(0, guess+1):
            if k not in ex_list:
                ex_list.append(k)
        line = ""
        for i in range(1, highest+1):
            if i in ex_list:
                line += "|{:4}".format(" ")
            else:
                line += "|{:4}".format(i)
            if i % 10 == 0:
                print(line+"|")
                line = ""
        if len(ex_list) == highest:
            print("Hurra! Hai vinto!! (☞ﾟヮﾟ)☞ \nIl numero era {}!".format(solution))
            break
        guess = int(input())
    elif guess > solution:
        for k in range(guess, highest+1):
            if k not in ex_list:
                ex_list.append(k)
        line = ""
        for i in range(1, highest+1):
            if i in ex_list:
                line += "|{:4}".format(" ")
            else:
                line += "|{:4}".format(i)
            if i % 10 == 0:
                print(line+"|")
                line = ""
        if len(ex_list) == highest:
            print("Hurra! Hai vinto!! (☞ﾟヮﾟ)☞\nIl numero era {}!".format(solution))
            break
        guess = int(input())
