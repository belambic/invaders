import sys, os, curses, traceback

class Display(object):
	def __init__(self):
		# Initialize curses
		self.screen = curses.initscr()

		# Turn off echoing of keys, and enter cbreak mode,
		# where no buffering is performed on keyboard input
		curses.noecho()
		curses.cbreak()
		curses.curs_set(0)

		# In keypad mode, escape sequences for special keys
		# (like the cursor keys) will be interpreted and
		# a special value like curses.KEY_LEFT will be returned
		self.screen.keypad(1)

		# No buffering
		self.screen.nodelay(1)

		# Pretty border
		self.border = 0

		# Get the size of the screen
		# @TODO make use of this
		self.height, self.width = self.screen.getmaxyx()

		self.refresh()

	# Refresh the screen
	def refresh(self):
		self.screen.border(self.border)
		self.screen.refresh()

	# Function to add a string to the screen
	def addStr(self, y, x, message):
		try:
			self.screen.addstr(y, x, str(message))
		except:
			self.close()
			traceback.print_exc(file=sys.stdout)
			print y
			print x
			print message
			exit()

	def putstring(self, y, x, str):
		self.addStr(y, x, str);
    
	# Function to move the cursor
	def move(self, y, x):
		self.screen.move(y,x)

	# Function to get a keypress
	def getch(self):
		try:
			return self.screen.getch()
		except:
			raise Exception("screen.getch raised !")

	def erase(self):
		self.screen.erase()
		
	# Close the screen and reset to sanity
	def close(self):
		self.screen.erase()
		self.screen.refresh()
		self.screen.keypad(0)
		curses.echo()
		curses.nocbreak()
		curses.endwin()
