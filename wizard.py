from actor import Actor

class Wizard(Actor):
	"""Example AI actor"""
	def __init__(self):
		super(Wizard, self).__init__()
		self.id = 1
		self.moves = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]