#CycloidClass

import numpy as np
import pygame
from pygame import *
from trig import *

def rotationMatrix(deg):
    return np.array([[fcos(deg),fsin(deg)],
                    [-fsin(deg),fcos(deg)]])

def getCoords(arr):
    return (arr[0][0],arr[1][0])

def translateCoords(coords,cx,cy):
    return(int(coords[0]+cx),int(coords[1]+cy))


class Trail():
    def __init__(self,circ,vec):
        self.circ = circ
        self.vec = vec
        self.points = []
        self.reps = 0
        self.drawing = True

    def update(self,DISPLAY,colScheme,WIDTH,HEIGHT,line,cir):
        self.circ.update()
        masterCoords = self.circ.draw(DISPLAY,colScheme[2],WIDTH,HEIGHT,cir)
        rotVec = rotationMatrix(self.circ.srotation+self.circ.rotation).dot(self.vec)
        newCoord = translateCoords(getCoords(rotVec),masterCoords[0],masterCoords[1])
        if self.drawing:
            h = newCoord in self.points
            if h:
                self.reps += 1
                if self.reps > 120:
                    self.drawing = False
            else:
                self.reps = 0
            self.points.append(newCoord)
        if len(self.points) > 1 and line:
            pygame.draw.lines(DISPLAY,colScheme[1],False,self.points,3)
        if self.drawing:
            if h:
                c = (0,240,0)
            else:
                c = (200,200,0)
        else:
            c = colScheme[1]
        pygame.draw.circle(DISPLAY,c,newCoord,7)

class Circle():
    def __init__(self,masterCycloid,r,rotVel,sRot,inv):
        self.r = r
        self.masterCycloid = masterCycloid
        if masterCycloid != None:
            masterCoords = getCoords(self.masterCycloid.pos)
            if inv:
                self.pos = np.array([[self.masterCycloid.r-self.r,0]]).T
            else:
                self.pos = np.array([[self.masterCycloid.r+self.r,0]]).T
        else:
            self.pos = np.array([[0,0]]).T
        self.rotation = 0
        self.rotVel = rotVel
        self.srotation = 0
        if sRot != None:
            if inv:
                self.sRot = -sRot
            else:
                self.sRot = sRot
        else:
            if inv:
                self.sRot = -self.rotVel
            else:
                self.sRot = self.rotVel


    def update(self):
        self.rotation += self.rotVel
        self.rotation = self.rotation%360
        if self.sRot != None:
            self.srotation += self.sRot
            self.srotation = self.srotation%360

        if self.masterCycloid:
            self.masterCycloid.update()

    def draw(self,DISPLAY,col,WIDTH,HEIGHT,cir):

        if self.masterCycloid:
            relCoords = self.masterCycloid.draw(DISPLAY,col,WIDTH,HEIGHT,cir)
            rotVec = rotationMatrix(self.rotation).dot(self.pos)
            realPos = relCoords+rotVec
            if cir:
                pygame.draw.circle(DISPLAY,col,getCoords(realPos.astype(int)),int(self.r),1)

            return realPos
        else:
            realPos = np.array([[int(WIDTH/2),int(HEIGHT/2)]]).T
            if cir:
                pygame.draw.circle(DISPLAY,col,getCoords(realPos),int(self.r),1)

            return realPos
