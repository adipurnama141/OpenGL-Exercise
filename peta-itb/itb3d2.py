import pyglet
from pyglet.gl import *
from pyglet.window import key
from OpenGL.GLUT import *
import sys, time, math, os, random
import Image

WINDOW   = 500
INCREMENT = 20
SMOOTH_INC = 5


def loadTexture(filename):
    img = Image.open(filename).transpose(Image.FLIP_TOP_BOTTOM)
    textureIDs = (pyglet.gl.GLuint * 1) ()
    glGenTextures(1,textureIDs)
    textureID = textureIDs[0]
    print 'generating texture', textureID, 'from', filename
    glBindTexture(GL_TEXTURE_2D, textureID)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.size[0], img.size[1],
                 0, GL_RGBA, GL_UNSIGNED_BYTE, img.tostring())
    glBindTexture(GL_TEXTURE_2D, 0)
    return textureID





class Window(pyglet.window.Window):

   # Cube 3D start rotation
   xRotation = yRotation = 30  
   def __init__(self, width, height, title=''):
       config = Config(sample_buffers=1, samples=4,depth_size=16, double_buffer=True,) 
       super(Window, self).__init__(width, height, title, config=config, vsync=False)
       glClearColor(0, 0, 0, 1)
       glEnable(GL_DEPTH_TEST) 
       self.x = -235
       self.y = -480
       self.z = 230
       self.xRotation = -215
       self.yRotation = -0
       self.zRotation = 0
       # self.x = -215
       # self.y = -60
       # self.z = -10
       # self.xRotation = -265
       # self.yRotation = -0
       # self.zRotation = 0
       self.textureList = []
       self.textureList.append(loadTexture("aula.png"))
       self.textureList.append(loadTexture("ctim.png"))
       self.textureList.append(loadTexture("road.png"))
       self.textureList.append(loadTexture("roof.png"))
       self.repeatFactor = 0.0
       self.currentBuilding = 1

   def next_building(self):
    self.currentBuilding += 1
    print self.currentBuilding

   def texture_config(self):
       if (self.currentBuilding < 5):
        glBindTexture(GL_TEXTURE_2D, self.textureList[0])
       elif (self.currentBuilding == 7):
        glBindTexture(GL_TEXTURE_2D, self.textureList[3])
       elif ((self.currentBuilding== 6) or (self.currentBuilding == 5)):
        glBindTexture(GL_TEXTURE_2D, self.textureList[1])

   def color_config(self):
       if (self.currentBuilding < 5):
        glColor3f(0.4, 0.4, 0.4);
       else:
        glColor3f(0.5, 0.5, 0.5);

        

   def on_mouse_motion(self,x,y,dx,dy):
       #self.xRotation += dx
       #self.yRotation += dy  
       pass

   def on_draw(self):
       # Clear the current GL Window
       self.clear()
       # Push Matrix onto stack
       glPushMatrix()
       glClearColor(0.8, 0.8, 0.8, 1.0)
       glClear(GL_COLOR_BUFFER_BIT)

       glRotatef(self.xRotation, 1, 0, 0)
       glRotatef(self.yRotation, 0, 1, 0)
       glRotatef(self.zRotation, 0,0,1)
       glTranslatef(self.x , self.y, self.z)


       with open("building.txt") as f:
        content = f.readlines()
       content = [x.strip() for x in content]

       
       startpoint = []
       endpoint = list(content[1].split())
       firstpoint  = []

       isFirst = True
       for i,val in enumerate(content):
         temp = val.split()
         if ((len(temp) == 2)):
           startpoint = list(endpoint)
           endpoint = list(temp)
           glEnable(GL_TEXTURE_2D)
           self.texture_config()
           glBegin(GL_QUADS)
           self.color_config()
           glTexCoord2f(5.0,1.0);
           glVertex3i(int(startpoint[0]),int(startpoint[1]),0)
           glTexCoord2f(5.0,0.0);
           glVertex3i(int(startpoint[0]),int(startpoint[1]),10)
           glTexCoord2f(0.0,0.0);
           glVertex3i(int(endpoint[0]),int(endpoint[1]),10)
           glTexCoord2f(0.0,1.0);
           glVertex3i(int(endpoint[0]),int(endpoint[1]),0)
           glEnd()
           glDisable(GL_TEXTURE_2D)
           if (isFirst):
            firstpoint = list(temp)
            isFirst = False
         elif ((i >1) and (len(temp) == 1)):
           glEnable(GL_TEXTURE_2D)
           self.texture_config()
           #glBindTexture(GL_TEXTURE_2D, self.textureList[1])
           glBegin(GL_QUADS)
           self.color_config()
           glTexCoord2f(50.0,1.0);
           glVertex3i(int(firstpoint[0]),int(firstpoint[1]),0)
           glTexCoord2f(50.0,0.0);
           glVertex3i(int(firstpoint[0]),int(firstpoint[1]),10)
           glTexCoord2f(0.0,0.0);
           glVertex3i(int(endpoint[0]),int(endpoint[1]),10)
           glTexCoord2f(0.0,1.0);
           glVertex3i(int(endpoint[0]),int(endpoint[1]),0)
           glEnd()
           glDisable(GL_TEXTURE_2D)
           isFirst = True
           startpoint = []
           endpoint = list(content[i+1].split())
           self.next_building()


       # glEnable(GL_TEXTURE_2D)
       # glBindTexture(GL_TEXTURE_2D, self.textureList[2])
       # glBegin(GL_QUADS)
       # glColor3f(0.35, 0.35, 0.35);
       # glTexCoord2f(200.0,200.0);
       # glVertex3i(0,0,0)
       # glTexCoord2f(200.0,0.0);
       # glVertex3i(0,500,10)
       # glTexCoord2f(0.0,0.0);
       # glVertex3i(500,500,10)
       # glTexCoord2f(0.0,200.0);
       # glVertex3i(500,0,0)
       # glEnd()
       # glDisable(GL_TEXTURE_2D)


       glPopMatrix()
       self.currentBuilding = 0

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

   def on_key_press(self,symbol,modifier):
    if symbol == key.Q:
     self.x += INCREMENT
    elif symbol == key.A:
     self.x -= INCREMENT
    elif symbol == key.W:
     self.z -= INCREMENT
    elif symbol == key.S:
     self.z += INCREMENT
    elif symbol == key.E:
     self.y += INCREMENT
    elif symbol == key.D:
     self.y -= INCREMENT
    elif symbol == key.R:
     self.zRotation += SMOOTH_INC
    elif symbol == key.F:
     self.zRotation -= SMOOTH_INC
    elif symbol == key.Z:
     print("r pressed" + str(self.x) +"-"+ str(self.y) +"-"+str(self.z) +"-"+ str(self.xRotation) + "-" + str(self.yRotation) + "-" + str(self.zRotation) )


   def on_text_motion(self, motion):
       if motion == key.UP:
            self.xRotation -= SMOOTH_INC
       elif motion == key.DOWN:
           self.xRotation += SMOOTH_INC
       elif motion == key.LEFT:
           self.yRotation -= SMOOTH_INC
       elif motion == key.RIGHT:
           self.yRotation += SMOOTH_INC
       





Window(WINDOW, WINDOW, 'Polytron Zap 4G')
pyglet.app.run()