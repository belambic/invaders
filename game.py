import traceback, time
from display import Display
from gun import Gun
from alien import Alien

class Game(object):
	def __init__(self):
		pass

	def status(self, display, lives, score, level):
		display.putstring(1, 1, "Score: " + str(score))
		display.putstring(1, 40, "Lives: " + str(lives))
		display.putstring(1, 70, "Level: " + str(level))
		
	def make_aliens(self, count, width, tick):
		aliens = []
		y=14
		x=4
		for alien in range(0, count):
			x = (4+alien*10) % (width-10)
			if not alien % (width/11):
				x = 4
				y -= 2
			aliens.append(Alien(y=y, x=x, tick=tick))
		return aliens
	 
	def start(self):
		score = 0
		lives = 3
		level = 1
		framerate = 25
		shields = 4
		alien_tick = 15
		gameover = False

		display = Display()
		gun = Gun(maxx=display.width, maxy=display.height)
		aliens = self.make_aliens(42, display.width, alien_tick)

		while True:
			self.status(display, lives, score, level)

			for alien in aliens:
				alien.move()
				display.putstring(alien.last[0], alien.last[1], "     ")
				display.putstring(alien.current[0], alien.current[1], alien.alien)

			display.putstring(gun.guny, gun.gunx, gun.gun)
			
			for index, alien in enumerate(aliens):
				hit = gun.hit(alien.current[0], alien.current[1])
				if hit:
					display.putstring(alien.current[0], alien.current[1], " BOOM ")
					score += 1
					del(aliens[index])
					break
				
				if alien.current[0] == display.height - 2:
					if lives > 0:
						lives -= 1
						aliens = self.make_aliens(42, display.width, alien_tick)
						display.erase()
					else:
						gameover = True
						display.putstring(10, 30, "Game Over!!!")
					break

			if aliens == []:
				display.putstring(10, 30, "YOU WIN!!!!")
				
			if gun.firing:
				gun.fire()
				display.putstring(gun.bullety, gun.bulletx, gun.bullet)
		
			display.refresh()
			time.sleep(1.0 / framerate)
			
			if gameover:
				display.close()
				break

			if gun.firing:
				display.putstring(gun.bullety, gun.bulletx, " ")

			if hit:
				display.putstring(alien.current[0], alien.current[1], "      ")
				
			if aliens == []:
				display.putstring(10, 30, "            ")
				level += 1
				alien_tick -= 1
				aliens = self.make_aliens(42, display.width, alien_tick)

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
			
