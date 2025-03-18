from tkinter import *
from snakeobj import *

mainwin = Tk()

canvas1=Canvas(mainwin,width=1080,height=2200, bg = "black")
canvas1.place(x=0, y=0)

snakealive = True
score=0
level=1
eat = False
direction = 0 # snake direction udlr
fruitlist = []
snake = []			  	

fontsmall = ("Arial",12)
scoretext = canvas1.create_text(1100,80,font=fontsmall,text="Score 0",fill="yellow")

leveltext = canvas1.create_text(300,80,font=fontsmall,text="Level 1",fill="yellow")		 	 		
		 
# playfield, 100 by 100
# use list comprehension and write about it
def create_matrix(rows,cols):
    return [[0 for i in range(cols)] for j in range(rows)]

grid = create_matrix(rows=100,cols=100) 
  		 	
def setgrid(sx,sy,gtype):
    gx = int(sx/head.bsize)
    gy = int(sy/head.bsize)
    grid[gy][gx] = gtype

def getgrid(sx,sy):
    gx = int(sx/head.bsize)
    gy = int(sy/head.bsize)     
    return grid[gy][gx]
 	 			 	 		 
head = headobj(canvas1,"headsU8.png","headsR8.png","headsD8.png","headsL8.png",x=9*8*10,y=9*8*14)
	
def makesnake():
 for i in range(1,10):
     sx = head.x
     sy = head.y+head.bsize*i
     part = gameobj(canvas1,"body8.png",x=head.x,y=sy)
     setgrid(sx,sy,1)
     snake.append(part)
 
makesnake()
						
def makefruit():
  for i in range(10):
      sx = (4+2*i)*head.bsize
      sy = 10*head.bsize
      fruit = gameobj(canvas1,"fruit8.png",x=sx,y=sy)
      fruitlist.append(fruit)
      setgrid(sx,sy,2)				     							
def removefruit(fx,fy):
	for f in fruitlist:
		if (f.x-fx)**2+(f.y-fy)**2 < 100:
		 f.undraw()
		 fruitlist.remove(f)
		 # do not remove, just list =[] at start of level							
def movesnake():
	global snake, snakealive, score, eat
	setgrid(snake[-1].x,snake[-1].y,0)
	if eat == False: 
	   snake[-1].undraw() # rm bottom
	   snake.pop() # remove bottom
	head.move()
	eat = False
	top = gameobj(canvas1,"body8.png",x=head.x-head.dx*head.bsize,y=head.y-head.bsize*head.dy)
	if getgrid(head.x, head.y) == 1:
	    snakealive = False
	if getgrid(head.x, head.y) == 2:
	    score = score + 1
	    eat = True
	    removefruit(head.x, head.y)	    
	setgrid(top.x,top.y,1)
	snake.insert(0,top) # add top	
									

makefruit()

def timerupdate():
	global direction
	canvas1.itemconfigure(scoretext,text="Score "+str(score))
	if direction == "l":
	    head.faceleft()
	elif direction == "u":
	    head.faceup()    
	elif direction == "r":
	    head.faceright()
	elif direction == "d":
	    head.facedown()
	if snakealive:
	    movesnake()
	direction = 0    	   	   
	mainwin.after(700,timerupdate)


def change_direction(new_direction):
    global direction
    direction = new_direction

btnup=Button(mainwin, text="u", command=lambda: change_direction("u"))
btnup.place(x=200, y=100)

btnright=Button(mainwin, text="r", command=lambda: change_direction("r"))
btnright.place(x=400, y=200)

btnleft=Button(mainwin, text = "l", command = lambda: change_direction("l"))
btnleft.place(x=00,y=200)

btndown = Button(mainwin, text = "d", command = lambda: change_direction("d"))
btndown.place(x=200,y=300)

timerupdate()
mainwin.mainloop()