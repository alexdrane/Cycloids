
#Cycloid drawing
import pygame
from pygame import *
import sys
from CycloidClass import Circle,Trail
import numpy as np
from math import *






def flip(array):
    newArray = []
    for i in range(len(array)):
        newArray.append(array[-(i+1)])
    return newArray


def askNum(msg):
    while True:
        try:
            num = float(input(msg))
        except:
            print("Failed")
        else:
            return num
            break

def mainCyc(WIDTH,HEIGHT,colScheme):

    line = True
    cir = True

    r1 = askNum("Radius 1: ")
    c1 = pi*(r1*2)
    print(c1)
    m = Circle(None,r1,0,None,None)
    inp = None
    while (inp != "E" and inp != "H"):
        inp = input("(E)picycloid/trochoid or (H)ypercycloid/trochoid: ").upper()
    if inp  == "E":
        inv = False
    else:
        inv = True
    r2 = askNum("Radius 2: ")
    c2 = pi*(r2*2)
    print(c2)
    s = askNum("Rate of rotation: ")
    ratio = c1/c2
    rot = s*ratio
    print(s,rot)
    circ = Circle(m,r2,s,rot,inv)
    x = askNum("Radius: ")
    trail = Trail(circ,np.array([[x,0]]).T)



    pygame.init()
    DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)

    while True:
        DISPLAY.fill(colScheme[0])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    colScheme = flip(colScheme)
                if event.key == K_t:
                    line = not line
                if event.key == K_c:
                    cir = not cir

        trail.update(DISPLAY,colScheme,WIDTH,HEIGHT,line,cir)

        pygame.display.update()


def mainVect(WIDTH,HEIGHT,colScheme):

    line = True
    cir = True

    prev = None
    while True:
        print("Press enter to add the next citcle, or T to add the trail")
        inp = input()
        if inp.upper() == "T":
            break
        else:
            print("Adding new circle")
            r = askNum("Radius: ")
            if prev == None:
                rot = 0
            else:
                rot = askNum("Rate of rotation: ")
            circ  = Circle(prev,r,rot,None,None)
            prev = circ
    x = askNum("X radius: ")
    y = askNum("Y radius: ")
    trail = Trail(circ,np.array([[x,y]]).T)


    car1 = Circle(None,150,0,None,None)
    car2 = Circle(car1,120,0.2,None,None)

    #trail = Trail(car2,np.array([[120,0]]).T)

    ran1 = Circle(None,150,0,None,None)
    ran2 = Circle(ran1,100,1.5,None,None)
    ran3 = Circle(ran2,50,-1,None,None)
    ran4 = Circle(ran3,40,3,None,None)
    ran5 = Circle(ran4,40,-1,None,None)
    ran6 = Circle(ran5,30,-0.1,None,None)
    ran7 = Circle(ran6,20,-2,None,None)

    #trail = Trail(ran7,np.array([[20,0]]).T)

    cyc1 = Circle(None,200,0,None,None)
    cyc2 = Circle(cyc1,120,0.1,None,None)
    cyc3 = Circle(cyc2,50,0.25,None,None)

    #trail = Trail(cyc3,np.array([[50,0]]).T)

    pygame.init()
    DISPLAY = pygame.display.set_mode((WIDTH,HEIGHT),FULLSCREEN)

    while True:
        DISPLAY.fill(colScheme[0])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_f:
                    colScheme = flip(colScheme)
                if event.key == K_t:
                    line = not line
                if event.key == K_c:
                    cir = not cir

        trail.update(DISPLAY,colScheme,WIDTH,HEIGHT,line,cir)

        pygame.display.update()


WIDTH,HEIGHT = int(input("WIDTH:  ")),int(input("HEIGHT:  "))
colScheme = [(255,255,255),(150,0,0),(0,0,20)]
inp = input("(C)ycloids or (S)eries: ").upper()
if inp == "C":
    mainCyc(WIDTH,HEIGHT,colScheme)
elif inp == "S":
    mainVect(WIDTH,HEIGHT,colScheme)
