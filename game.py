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

		display = Display()
		gun = Gun(maxx=display.width, maxy=display.height)
		alien = Alien(maxx=display.width, maxy=display.height)
		position = alien.move()
		
		while True:
			old_position = position
			position = alien.move()
		
			display.putstring(old_position[0], old_position[1], "     ")
	
			self.status(display, lives, score)
			display.putstring(position[0], position[1], alien.alien)
			display.putstring(gun.guny, gun.gunx, gun.gun)
			hit = gun.hits(alien.Y, alien.X)

			if alien.Y == display.height - 2:
				if lives == 1:
					lives -= 1
					display.putstring(alien.Y, alien.X, "     ")
					alien.reset()
				else:
					gameover = True
					display.putstring(10, 30, "Game Over!!!")
					display.putstring(alien.Y, alien.X, "     ")
					alien.reset()
			elif hit:
				display.putstring(alien.Y, alien.X, " BOOM ")
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
				display.putstring(alien.Y, alien.X, "      ")
				alienX = 0
				alienY = 5

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
			
