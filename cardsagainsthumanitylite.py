#Cards Against Humanity Lite ver 1.0

white = ("Screaming Monkeys.", "Fabulous Elephants.", "Trumps Wig.", "Giant Midgets.", "Rabid Bunnies.")
black = ("How did I lose my virginity? : ", "What's that sound? : ", "I drink to forget : ")


from random import randrange, uniform

randwhite = randrange(0, 5)
randblack = randrange(0,3)

print(black[randblack] + white[randwhite])