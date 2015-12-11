# buttongame.py
# This game will display 3 buttons. One will be a winner. If you click the correct
# button, you win! If not, you lose. Sorry. :\

from gbutton import GButton
from random import randrange
from graphics import *

def main():
	nwins = 0
	nlosses = 0

	# Draw the window.
	win = GraphWin("Three Button Monty",800,600)
	win.setCoords(0,0,4,2)
	win.setBackground("lightblue")
	wint = Text(Point(.5,1.9), "   Wins: %d" % nwins)
	losst = Text(Point(.5,1.8), "Losses: %d" % nlosses)
	wint.setSize(20)
	wint.setTextColor("darkblue")
	losst.setSize(20)
	losst.setTextColor("red")
	wint.draw(win)
	losst.draw(win)
	
	# Draw the buttons.
	quitButton = GButton(win,Point(3.5,.3),.6,.3,"Quit")
	resetButton = GButton(win,Point(.5,.3),.6,.3,"Reset")
	button1 = GButton(win,Point(1,1),1,.8,"1")
	button2 = GButton(win,Point(2,1),1,.8,"2")
	button3 = GButton(win,Point(3,1),1,.8,"3")
	
	# Initialize the winning button and deactivate Reset button.
	resetButton.deactivate()
	w = randrange(1,4)
	if w == 1:
		button1.winButton()
		
	elif w == 2:
		button2.winButton()
		
	else:
		button3.winButton()
		
	#Start the game loop.
	pt = win.getMouse()
	
	while not quitButton.clicked(pt):
		
		# Checks for which button is pushed
		if button1.clicked(pt):
			g = button1.getWin()
			button2.getWin()
			button3.getWin()
			
			if g == True:
				ltxt = Text(Point(2,1.5),"YOU WIN")
				ltxt.setFill("darkblue")
				ltxt.setStyle("bold")
				ltxt.draw(win)
				nwins += 1
			
			else:
				ltxt = Text(Point(2,1.5),"YOU LOSE")
				ltxt.setFill("red")
				ltxt.setStyle("bold")
				ltxt.draw(win)
				nlosses += 1
				
			button1.deactivate()
			button2.deactivate()
			button3.deactivate()
				
			resetButton.activate()
			
		elif button2.clicked(pt):
			g = button2.getWin()
			button1.getWin()
			button3.getWin()
			
			if g == True:
				ltxt = Text(Point(2,1.5),"YOU WIN")
				ltxt.setFill("darkblue")
				ltxt.setStyle("bold")
				ltxt.draw(win)
				nwins += 1
			
			else:
				ltxt = Text(Point(2,1.5),"YOU LOSE")
				ltxt.setFill("red")
				ltxt.setStyle("bold")
				ltxt.draw(win)
				nlosses += 1
				
			button1.deactivate()
			button2.deactivate()
			button3.deactivate()
				
			resetButton.activate()
			
		elif button3.clicked(pt):
			g = button3.getWin()
			button1.getWin()
			button2.getWin()
			
			if g == True:
				ltxt = Text(Point(2,1.5),"YOU WIN")
				ltxt.setFill("darkblue")
				ltxt.setStyle("bold")
				ltxt.draw(win)
				nwins += 1
			
			else:
				ltxt = Text(Point(2,1.5),"YOU LOSE")
				ltxt.setFill("red")
				ltxt.setStyle("bold")
				ltxt.draw(win)
				nlosses += 1
				
			button1.deactivate()
			button2.deactivate()
			button3.deactivate()
				
			resetButton.activate()
			
		elif resetButton.clicked(pt):
			ltxt.undraw()
			button1.reset()
			button2.reset()
			button3.reset()
			w = randrange(1,4)			#Reinitializes the random button
			
			if w == 1:
				button1.winButton()
				
			elif w == 2:
				button2.winButton()
				
			else:
				button3.winButton()
				
			resetButton.deactivate()
			button1.activate()
			button2.activate()
			button3.activate()
			
		wint.setText("   Wins: %d" % nwins)
		losst.setText("Losses: %d" % nlosses)
		pt = win.getMouse()
		
	win.close()
	
main()