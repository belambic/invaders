import time

class Gun(object):
	def __init__(self, maxy, maxx):
		self.maxx = maxx
		self.maxy = maxy
		self.gunx = maxx / 2
		self.guny = maxy - 2
		self.firing = False
		self.bullet = "|"
		self.gun = " _A_ "

	def start(self):
		if not self.firing:
			self.firing = True
			self.bulletx = self.gunx + 2
			self.bullety = self.maxy - 2

	def left(self):
		if self.gunx > 0:
			self.gunx -= 1

	def right(self):
		if self.gunx < self.maxx - 5:
			self.gunx += 1

	def fire(self):
		if self.firing:
			self.bullety -= 1
			if self.bullety == 0:
				self.firing = False
	
	def hit(self, y, x):
		if self.bullety == y and self.bulletx >= x and self.bulletx <= x + 3:
			self.firing = False
			return True
		
	def hits(self, alieny, alienx):
		ret = False
		if self.firing:
			self.fire()
			ret = self.hit(alieny, alienx)
		return ret
