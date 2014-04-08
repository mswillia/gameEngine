class Node(object):
	"""Map node object."""
	def __init__(self, type, location, actors):
		self.location = location
		self.type = type
		self.actors = actors
		
	def isPassable(self):
		return type != -1
		
	def removeActor(self, actor):
		self.actors.remove(actor)
		actor.setNode(None)
		
	def addActor(self, actor):
		self.actors.append(actor)
		actor.setNode(self)