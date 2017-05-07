import pyglet
from pyglet.window import key
from pyglet.gl import *

win = pyglet.window.Window()
win.set_fullscreen(False)

global xRotation
global yRotation

xRotation = 0
yRotation = 0
INCREMENT = 20

@win.event
def on_init():
	glClear(GL_COLOR_BUFFER_BIT)
	glClearColor(1, 1, 1, 1)
	glEnable(GL_DEPTH_TEST)

@win.event
def on_key_press(symbol,modifier):
	global xRotation
	global yRotation
	if symbol == key.UP:
		xRotation -= INCREMENT
	elif symbol == key.DOWN:
		xRotation += INCREMENT
	elif symbol == key.LEFT:
		yRotation -= INCREMENT
	elif symbol == key.RIGHT:
		yRotation += INCREMENT
	elif symbol == key.R:
		print("r pressed")
		xRotation = 0
		yRotation = 0


@win.event
def on_draw():
	#Clear buffer
	#glEnable(GL_DEPTH_TEST)
	glRotatef(xRotation, 1, 0, 0)
	glRotatef(yRotation, 0, 1, 0)

	glClear(GL_COLOR_BUFFER_BIT)
	itsfirst = False
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1.0, 0, 0);
	with open("building.txt") as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	firstpoint = [0,0]
	for i,val in enumerate(content):
		temp = val.split()
		if (len(temp) == 2):
		  glVertex3i(int(temp[0]),int(temp[1]),0)
		  if (itsfirst == True):
		  	firstpoint = list(temp)
		  	itsfirst = False
		else:
			glVertex2i(int(firstpoint[0]),int(firstpoint[1]))
			glEnd()
			glBegin(GL_TRIANGLE_FAN)
			itsfirst = True
	glEnd()

	
pyglet.app.run()