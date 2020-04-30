if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")

# la stringa vuota è valutato sempre false. di conseguenza, if name: controlla che name non sia vuota
# if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name")
