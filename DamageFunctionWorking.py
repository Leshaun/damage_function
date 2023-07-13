from random import randint


class Moves:
    def __init__(self, min, max):
        self.min = min
        self.max = max


moves = [
    Moves(1, 3),
    Moves(5, 8),
    Moves(2, 20)
]

def dmg_func(moves):
    dmg = randint(moves.min, moves.max)
    print(dmg)
    return dmg

hp = 20
hp = hp - dmg_func(moves[2])
print(hp)

hp = hp - dmg_func(moves[0])
print(hp)

hp = hp - dmg_func(moves[1])
print(hp)
