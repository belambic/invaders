import traceback, time
from display import Display
from gun import Gun

class Game(object):
	def __init__(self):
		pass

	def start(self):
		alienYincrement = 1
		alienXincrement = 1
		alienX = 0
		alienY = 5
		score = 0
		lives = 3
		framerate = 25
		shields = 4

		display = Display()
		gun = Gun(maxx=display.width, maxy=display.height)

		while True:
			if alienX == 0:
				alienXincrement = 1
				alienYincrement = 1
			elif alienX == display.width - 4:
				alienXincrement = -1
				alienYincrement = 1
			else:
				alienYincrement = 0
	
			if alienYincrement:
				display.putstring(alienY, alienX, "	 ")
		
			alienX += alienXincrement
			alienY += alienYincrement
	
			display.putstring(1, 1, score)
			display.putstring(alienY, alienX, " MwM ")
			display.putstring(gun.guny, gun.gunx, gun.gun)
			hit = gun.hits(alienY, alienX)

			if hit:
				display.putstring(alienY, alienX, " BOOM ")
				score += 1
			elif gun.firing:
				display.putstring(gun.bullety, gun.bulletx, gun.bullet)
		
			display.refresh()
			time.sleep(1.0 / framerate)

			if gun.firing:
				display.putstring(gun.bullety, gun.bulletx, " ")

			if hit:
				display.putstring(alienY, alienX, "      ")
				alienX = 0
				alienY = 5

			display.refresh()
	
			i = display.getch()
			if i == ord("a"):
				gun.left()
			elif i == ord ("d"):
				gun.right()
			elif i == ord("q"):
				display.close()
				break
			elif i == ord ("s"):
				gun.start()
