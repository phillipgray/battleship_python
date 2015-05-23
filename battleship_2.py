from bs_module import *

test = GameBoard(10)

ship0 = Ship("aircraft carrier")
ship1 = Ship("destroyer")
ship2 = Ship("aircraft carrier")
ship3 = Ship("submarine")
ship4 = Ship("patrol boat")

fleet = [ship0, ship1, ship2, ship3, ship4]
for ship in fleet:
    ship.set_location(test.all_spaces)

print Ship.occupied_spaces