from game import Game
from wizard import Wizard
from node import Node

size = 8
actors = [Wizard() for x in range(4)]
map = [[Node(0, (y, x), []) for x in range(size)] for y in range(size)]
map[2][2].addActor(actors[0])
map[2][6].addActor(actors[1])
map[6][2].addActor(actors[2])
map[7][7].addActor(actors[3])


state = Game(map,actors)

print state.toString()
print state.prob(actors[0])
state.updateMoves()
print state.toString()
print state.prob(actors[0])
state.updateMoves()
print state.toString()
print state.prob(actors[0])

