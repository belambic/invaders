class Alien(object):
	def __init__(self, y, x):
		self.startx = x
		self.starty = y
		self.X = x
		self.Y = y
		self.counter = 0
		self.tick = 15
		self.alien1 = " MwM "
		self.alien2 = " WmW "
		self.alien = self.alien1

	def move(self):
		self.counter += 1
		if self.counter == self.tick:
			self.counter = 0
		
			if self.X == self.startx:
				self.direction = 1
			elif self.X == self.startx + 7:
				self.direction = -1
			
			if self.X % 2:
				self.alien = self.alien1
			else:
				self.alien = self.alien2
				
			self.X += self.direction
				
		return [self.Y, self.X]


