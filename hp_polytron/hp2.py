import pyglet
import OpenGL
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
import sys, time, math, os, random
import Image

WINDOW   = 400
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
    #img.size[0]
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1],
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
    glBindTexture(GL_TEXTURE_2D, 0)
    return textureID





class Window(pyglet.window.Window):

   # Cube 3D start rotation
   xRotation = yRotation = 30  

   def __init__(self, width, height, title=''):
       super(Window, self).__init__(width, height, title)
       glClearColor(0, 0, 0, 1)
       glEnable(GL_DEPTH_TEST)  

   def on_draw(self):
       # Clear the current GL Window
       self.clear()

       # Push Matrix onto stack
       glPushMatrix()

       glRotatef(self.xRotation, 1, 0, 0)
       glRotatef(self.yRotation, 0, 1, 0)

       glEnable(GL_TEXTURE_2D)
       glBindTexture(GL_TEXTURE_2D, texture)
       glBegin(GL_QUADS)

       #glColor3ub(255, 0, 0)
       glTexCoord2f(0.0,0.0);
       glVertex3f(-50,-50,-50)
       glTexCoord2f(1.0,0.0);
       glVertex3f(40,-50,-50) 
       glTexCoord2f(1.0,1.0);
       glVertex3f(40,110,-50)
       glTexCoord2f(0.0,1.0);
       glVertex3f(-50,110,-50)


       glEnd()
       glDisable(GL_TEXTURE_2D)

     
       glEnable(GL_TEXTURE_2D)
       glBindTexture(GL_TEXTURE_2D, texture2)
       glBegin(GL_QUADS)
       glTexCoord2f(1.0,0.0);
       glVertex3f(40,-50,-42)
       glTexCoord2f(1.0,1.0);
       glVertex3f(40,110,-42)
       glTexCoord2f(0.0,1.0);
       glVertex3f(-50,110,-42)
       glTexCoord2f(0.0,0.0);
       glVertex3f(-50,-50,-42)
       glEnd()
       glDisable(GL_TEXTURE_2D)


       glEnable(GL_TEXTURE_2D)
       glBindTexture(GL_TEXTURE_2D, texture3)
       glBegin(GL_QUADS)
       glTexCoord2f(0.0,1.0);
       glVertex3f(40,-50,-42)
       glTexCoord2f(0.0,0.0);
       glVertex3f(40,-50,-50)
       glTexCoord2f(1.0,0.0);
       glVertex3f(40,110,-50)
       glTexCoord2f(1.0,1.0);
       glVertex3f(40,110,-42)
       glEnd()
       glDisable(GL_TEXTURE_2D)


       glEnable(GL_TEXTURE_2D)
       glBindTexture(GL_TEXTURE_2D, texture4)
       glBegin(GL_QUADS)
       glTexCoord2f(0.0,1.0);
       glVertex3f(-50,-50,-42)
       glTexCoord2f(0.0,0.0);
       glVertex3f(-50,-50,-50)
       glTexCoord2f(1.0,0.0);
       glVertex3f(-50,110,-50)
       glTexCoord2f(1.0,1.0);
       glVertex3f(-50,110,-42)
       glEnd()
       glDisable(GL_TEXTURE_2D)


       glEnable(GL_TEXTURE_2D)
       glBindTexture(GL_TEXTURE_2D, texture6)
       glBegin(GL_QUADS)
       glTexCoord2f(1.0,0.0);
       glVertex3f(40,-50,-50)
       glTexCoord2f(0.0,0.0);
       glVertex3f(-50,-50,-50)
       glTexCoord2f(0.0,1.0);
       glVertex3f(-50,-50,-42)
       glTexCoord2f(1.0,1.0);
       glVertex3f(40,-50,-42)
       glEnd()
       glDisable(GL_TEXTURE_2D)

       glEnable(GL_TEXTURE_2D)
       glBindTexture(GL_TEXTURE_2D, texture5)
       glBegin(GL_QUADS)
       glTexCoord2f(1.0,0.0);
       glVertex3f(40,110,-50)
       glTexCoord2f(0.0,0.0);
       glVertex3f(-50,110,-50)
       glTexCoord2f(0.0,1.0);
       glVertex3f(-50,110,-42)
       glTexCoord2f(1.0,1.0);
       glVertex3f(40,110,-42)
       glEnd()
       glDisable(GL_TEXTURE_2D)
       



       # Pop Matrix off stack
       glPopMatrix()

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