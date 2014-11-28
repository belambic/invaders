import traceback, time
from display import Display
from gun import Gun
from alien import Alien

class Game(object):
	def __init__(self):
		pass

	def status(self, display, lives, score):
		display.putstring(1, 1, "Score: " + str(score))
		display.putstring(1, 40, "Lives: " + str(lives))
        
	def start(self):
		score = 0
		lives = 3
		framerate = 25
		shields = 4
		gameover = False
		aliens = []
		positions = []
		old_positions = []

		display = Display()
		gun = Gun(maxx=display.width, maxy=display.height)

		y=5
		for aliencount in range(0, 14):
			x = 5+aliencount*10
			if x > display.width - 10:
				x -= 70
				y = 7
			aliens.append(Alien(y=y, x=x))
			positions.append(aliens[aliencount].move())
			old_positions.append(0)

		while True:
			self.status(display, lives, score)

			for aliencount in range(0, 14):
				old_positions[aliencount] = positions[aliencount]
				positions[aliencount] = aliens[aliencount].move()
				display.putstring(old_positions[aliencount][0], old_positions[aliencount][1], "     ")
				display.putstring(positions[aliencount][0], positions[aliencount][1], aliens[0].alien)

			display.putstring(gun.guny, gun.gunx, gun.gun)
			hit = gun.hits(aliens[0].Y, aliens[0].X)

			if aliens[0].Y == display.height - 2:
				if lives == 1:
					lives -= 1
					display.putstring(alien.Y, alien.X, "     ")
				else:
					gameover = True
					display.putstring(10, 30, "Game Over!!!")
					display.putstring(aliens[0].Y, aliens[0].X, "     ")
			elif hit:
				display.putstring(aliens[0].Y, aliens[0].X, " BOOM ")
				score += 1
			elif gun.firing:
				display.putstring(gun.bullety, gun.bulletx, gun.bullet)
		
			display.refresh()
			time.sleep(1.0 / framerate)
			
			if gameover:
				time.sleep(5)
				gameover = False
				display.putstring(10, 30, "            ")

			if gun.firing:
				display.putstring(gun.bullety, gun.bulletx, " ")

			if hit:
				display.putstring(aliens[0].Y, aliens[0].X, "      ")

			display.refresh()
	
			i = display.getch()
			if i == ord("a"):
				gun.left()
			elif i == ord("d"):
				gun.right()
			elif i == ord("s"):
				gun.start()
			elif i == ord("q"):
				display.close()
				break
			
