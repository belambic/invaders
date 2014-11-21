class Alien(object):
	def __init__(self, maxy, maxx):
		self.maxx = maxx
		self.maxy = maxy
		self.alienYincrement = 1
		self.alienXincrement = 1
		self.reset()
		self.alien = " MwM "

	def move(self):
		if self.X == 0:
			self.alienXincrement = 1
			self.alienYincrement = 1
		elif self.X == self.maxx - 4:
			self.alienXincrement = -1
			self.alienYincrement = 1
		else:
			self.alienYincrement = 0
				
		self.X += self.alienXincrement
		self.Y += self.alienYincrement
		
		return [self.Y, self.X]
		
	def reset(self):
		self.X = 0
		self.Y = 5
	


