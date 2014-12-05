class Alien(object):
	def __init__(self, y, x, tick):
		self.start = (y,x)
		self.current = (y,x)
		self.last = (y,x)
		self.direction = 1
		self.counter = 0
		self.tick = tick
		self.range = 7
		self.alien1 = " MwM "
		self.alien2 = " WmW "
		self.alien = self.alien1

	def move(self):
		self.last = self.current
		self.counter += 1
		y = self.current[0]
					
		if self.counter == self.tick:
			self.counter = 0
		
			if self.start[1] == self.current[1]:
				self.direction = 1
				y += 1
			elif self.current[1] == self.start[1] + self.range:
				self.direction = -1
				y += 1
			
			if self.current[1] % 2:
				self.alien = self.alien1
			else:
				self.alien = self.alien2
				
			self.current = (y, self.current[1] + self.direction)
