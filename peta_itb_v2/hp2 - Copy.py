import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
import sys, time, math, os, random
import Image

WINDOW   = 1000
INCREMENT = 5



def loadTexture(filename):
    img = Image.open(filename).transpose(Image.FLIP_TOP_BOTTOM)
    textureIDs = (pyglet.gl.GLuint * 1) ()
    glGenTextures(1,textureIDs)
    textureID = textureIDs[0]
    print 'generating texture', textureID, 'from', filename
    glBindTexture(GL_TEXTURE_2D, textureID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1],
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
    glBindTexture(GL_TEXTURE_2D, 0)
    return textureID





class Window(pyglet.window.Window):

   # Cube 3D start rotation
   xRotation = yRotation = 30  

   def __init__(self, width, height, title=''):
       super(Window, self).__init__(width, height, title)
       self.set_fullscreen(True)
       glClearColor(0, 0, 0, 1)
       glEnable(GL_DEPTH_TEST)  

   def on_draw(self):
    self.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    with open("building.txt") as f:
      content = f.readlines()
    content = [x.strip() for x in content]
    glBegin(GL_LINE_STRIP)
    for i,val in enumerate(content):
      temp = val.split()
      if (len(temp) == 2):
        glColor3f(1.0, 1.0, 0);
        glVertex3f(float(temp[0]),float(temp[1]),300)
        print temp
      else:
        glEnd()
        glBegin(GL_LINE_STRIP)

    glVertex2i(133,466)
    glVertex2i(239,475)
    glVertex2i(263,525)
    glVertex2i(227,543)  
    glEnd()

    glBegin(GL_QUADS)
    glVertex2i(133,466)
    glVertex2i(239,475)
    glVertex2i(263,525)
    glVertex2i(227,543)  
    glEnd()
       

   def on_resize(self, width, height):
       # set the Viewport
       glViewport(0, 0, width, height)

       # using Projection mode
       glMatrixMode(GL_PROJECTION)
       glLoadIdentity()

       aspectRatio = width / height
       gluPerspective(35, aspectRatio, 1, 1000)

       glMatrixMode(GL_MODELVIEW)
       glLoadIdentity()
       glTranslatef(0, 0, -400)


   def on_text_motion(self, motion):
       if motion == key.UP:
            self.xRotation -= INCREMENT
       elif motion == key.DOWN:
           self.xRotation += INCREMENT
       elif motion == key.LEFT:
           self.yRotation -= INCREMENT
       elif motion == key.RIGHT:
           self.yRotation += INCREMENT





        
texture = loadTexture("2.png")
texture2 = loadTexture("dpn.png")
texture3 = loadTexture("kiri.png")
texture4 = loadTexture("kanan.png")
texture5 = loadTexture("bawah.png")
texture6 = loadTexture("atas.png")
Window(WINDOW, WINDOW, 'Polytron Zap 4G')
pyglet.app.run()