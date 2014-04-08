class Game(object):
	def __init__(self, map, actors):
		self.map = map
		self.actors = actors
		self.probmap = map = [[[0 for x in range(len(map[0]))] for y in range(len(map))] for a in range(len(actors))]
		for i in range(len(self.actors)):
			if self.actors[i].node != None:
				x,y = self.actors[i].node.location
				self.probmap[i][x][y] = 1.0
	
	def updateMoves(self):
		for actor in self.actors:
			x,y = actor.randomMove()
			i,j = actor.node.location
			if (i+x < len(self.map) and j+y < len(self.map[0])):
				self.map[i][j].removeActor(actor)
				self.map[i+x][j+y].addActor(actor)
			else:
				print "Move error"
			
	def prob(self, actor):
		a = self.actors.index(actor)
		ret = ''
		for i in range(len(self.probmap[a])):
			for j in range(len(self.probmap[a][i])):
				ret += '[' + str(self.probmap[a][i][j]) + '] '
			ret += '\n'
		return ret
		
	def toString(self):
		ret = ''
		for i in range(len(self.map)):
			for j in range(len(self.map[i])):
				ret += '[' + str(len(self.map[i][j].actors)) + '] '
			ret += '\n'
		return ret