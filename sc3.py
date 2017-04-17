import pyglet
from pyglet.gl import *
from math import *

window = pyglet.window.Window()

sky = pyglet.graphics.vertex_list(4,
    ('v2i', (0, 0,  700, 0, 700, 500, 0, 500)),
    ('c3B', (165, 220, 230,
     165, 220, 230, 
     0, 83, 176,  
     0, 83, 176)))

mountain = pyglet.graphics.vertex_list(3,
    ('v2i', 
    	(0, 0,
      600, 0, 
      300, 200 
    )),
    ('c3B', 
    	(160, 160, 17, 
    	160, 160, 17,
    	27, 27, 32)))


mountain2 = pyglet.graphics.vertex_list(3,
    ('v2i', 
    	(200, 0,
      800, 0, 
      550, 200 
    )),
    ('c3B', 
    	(27, 27, 32, 
    	160, 160, 17,
    	27, 27, 32)))


wood = pyglet.graphics.vertex_list(4,
    ('v2i', (15, 0,  30, 0, 30, 150, 15, 150)),
    ('c3B', (100, 77, 41,
     0, 0, 0, 
     100, 77, 41,  
     0, 0, 0)))


leaf = pyglet.graphics.vertex_list(3,
    ('v2i', 
    	(0, 50,
      50, 50, 
      20, 230 
    )),
    ('c3B', 
    	(143, 160, 12, 
    	22, 58, 0,
    	71, 102, 0)))

def makeCircle():
	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/200 * 360)
		x = 50 * cos(angle) + 80
		y = 50 * sin(angle) + 450
		verts += [x,y]
		colors += [251,199,5]
	glColor3f(1,1,0)
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)



def makeRainbow():
	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) + 30
		verts += [x,y]
		colors += [255-i,0,0]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)

	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) + 10
		verts += [x,y]
		colors += [255,255-i,0]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)


	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) + 10
		verts += [x,y]
		colors += [255,255-i,0]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)

	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) - 10
		verts += [x,y]
		colors += [255,255,0]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)

	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) - 30
		verts += [x,y]
		colors += [0,255-i,0]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)

	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) - 50
		verts += [x,y]
		colors += [0,0,255-i]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)

	verts = []
	colors = []
	for i in range(200):
		angle = radians(float(i)/400 * 360)
		x = 300 * cos(angle) + 500
		y = 300 * sin(angle) - 70
		verts += [x,y]
		colors += [107, 172, 211]
	circle = pyglet.graphics.vertex_list(200, ('v2f' , verts), ('c3B' , colors))
	circle.draw(GL_POLYGON)





@window.event
def on_draw():
    window.clear()
    sky.draw(pyglet.gl.GL_QUADS)
    
    makeRainbow()
    mountain2.draw(pyglet.gl.GL_TRIANGLES)
    mountain.draw(pyglet.gl.GL_TRIANGLES)
    wood.draw(pyglet.gl.GL_QUADS)
    leaf.draw(pyglet.gl.GL_TRIANGLES)
    makeCircle()



if __name__ == "__main__":
    pyglet.app.run()