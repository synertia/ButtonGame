# gbutton.py

"""This module will create buttons for the 3 button monty game and include
a variable to designate the button as a 'winner' or 'loser'"""

from graphics import *

class GButton:
	"""This creates buttons to be used for the 3 button monty game with win
	and loss triggers.
	e.g. gb = gButton(MyWin, Point(4,5), 5, 3,'Quit')"""
	
	def __init__(self,win,position,width,height,label):
		w,h = width/2.0 ,height/2.0
		x,y = position.getX(), position.getY()
		self.xmax,self.xmin = x+w,x-w
		self.ymax,self.ymin = y+h,y-h
		p1 = Point(self.xmin,self.ymin)
		p2 = Point(self.xmax,self.ymax)
		self.rect = Rectangle(p1,p2)
		self.rect.setFill("lightgray")
		self.rect.draw(win)
		self.label = Text(position,label)
		self.label.draw(win)
		self.winner = False
		self.activate()
		
	def clicked(self,p):
		"""Returns if the button is clicked in the graphic window."""
		return self.active and self.xmin<=p.getX()<=self.xmax and self.ymin<=p.getY()<=self.ymax
		
	def winButton(self):
		"""Changes the button to be a 'winning' button."""
		self.winner = True
		
	def getWin(self):
		"""Returns if the button is a winner or not."""
		if self.winner ==  True:
			self.rect.setFill("green")
			return True
			
		else:
			self.rect.setFill("red")
			return False
		
	def activate(self):
		"""Sets the button to 'active'"""
		self.label.setFill("black")
		self.active = True
		
	def deactivate(self):
		"""Sets a button to 'inactive'."""
		self.label.setFill("darkgray")
		self.active = False
		
	def reset(self):
		"""Resets the button."""
		self.rect.setFill("lightgray")
		self.winner = False