import random

class Actor(object):
	"""AI actor base class. Do not directly use in game"""
	def __init__(self):
		self.id = 0
		self.moves = [(0,0)]
		self.node = None
		
	def randomMove(self):
		return random.choice(self.moves)
		
	def setNode(self, node):
		self.node = node