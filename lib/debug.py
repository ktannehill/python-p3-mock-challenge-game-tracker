#!/usr/bin/env python3
# import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

player1 = Player("Kat")
player2 = Player("Mike")
player3 = Player("Serina")
player4 = Player("Brandon")

game1 = Game("Animal Crossing")
game2 = Game("Burnout 3")
game3 = Game("Katamari")

result1 = Result(player1, game1, 4999)
result2 = Result(player2, game1, 100)
result3 = Result(player1, game2, 1000)
result3 = Result(player1, game2, 300)
result4 = Result(player2, game3, 500)

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

print("May the odds be ever in your favor")
    # ipdb.set_trace()
