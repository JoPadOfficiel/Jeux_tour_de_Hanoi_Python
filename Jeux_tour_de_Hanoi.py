#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 23:35:23 2020

@author: JoPad
"""

#ring = anneau
import turtle
import colorsys
import math

turtle.setup(1100,600)
turtle.hideturtle()
turtle.title("Tour de Hanoï")
turtle.speed(0)
turtle.tracer(0,0)

n = 3
peg_height = 150
ring_height_max = 5
ring_width_max = 75
ring_width_min = 10
ring_delta = 7
ring_delta_max = 15
ring_height = 10
animation_step = 7



A = [] 
B = []
C = []
T = []



def dessiner_une_ligne(x,y,heading,length,pensize,color):
   turtle.up()
   turtle.goto(x,y)
   turtle.seth(heading)
   turtle.down()
   turtle.color(color)
   turtle.pensize(pensize)
   turtle.fd(length)

def dessiner_une_scène():
   turtle.bgcolor("white")
   dessiner_une_ligne(-450,-100,0,900,7.5,"brown")
   for i in range(-250,251,250):
       dessiner_une_ligne(i,-94,90,peg_height,5,"brown")

def initialiser():
   global ring_width_max,ring_width_min,ring_ratio,ring_delta
   for i in range(n):
       A.append(i)
       t = turtle.Turtle()
       t.hideturtle()
       t.speed(0)
       t.pencolor("black")
       t.fillcolor("black")
       T.append(t)
   ring_delta = min(135/(n-1),ring_delta_max)

def dessiner_un_seul_anneau(r, x, k, extra=0):
   global ring_delta
   w = ring_width_max - ring_delta*(r-1)
   T[r].up()
   T[r].goto(x-w/2,-95+ring_height*k + extra)
   T[r].down()
   T[r].seth(0)
   T[r].begin_fill()
   for i in range(2):
       T[r].fd(w)
       T[r].left(90)
       T[r].fd(ring_height)
       T[r].left(90)
   T[r].end_fill()

def dessiner_des_anneaux():
   for i in range(len(A)):
       dessiner_un_seul_anneau(A[i],-250,i)
   for i in range(len(B)):
       dessiner_un_seul_anneau(B[i],0,i)
   for i in range(len(C)):
       dessiner_un_seul_anneau(C[i],250,i)

def move_ring(PP,QQ):
   if PP == "A":
       x = -250
       P = A
   elif PP == "B":
       x = 0
       P = B
   else:
       x = 250
       P = C

   if QQ =="A":
       x2 = -250
       Q = A
   elif QQ == "B":
       x2 = 0
       Q = B
   else:
       x2 = 250
       Q = C

   for extra in range(1,100-(-95+ring_height*(len(P)-1)),animation_step):
       T[P[len(P)-1]].clear()
       dessiner_un_seul_anneau(P[len(P)-1],x,len(P)-1,extra)
       turtle.update()

   T[P[len(P)-1]].clear()
   dessiner_un_seul_anneau(P[len(P)-1],x,len(P)-1,extra)
   turtle.update()
   tp = x
   if x2 > x:
       step = animation_step
   else:
       step = -animation_step
   for tp in range(x,x2,step):
       T[P[len(P)-1]].clear()
       dessiner_un_seul_anneau(P[len(P)-1],tp,len(P)-1,extra)
       turtle.update()
   T[P[len(P)-1]].clear()
   dessiner_un_seul_anneau(P[len(P)-1],x2,len(P)-1,extra)
   turtle.update()
   Q.append(P[len(P)-1])
   del P[-1]
   for extra in range(100-(-95+ring_height*(len(Q)-1)),0,-animation_step):
       T[Q[len(Q)-1]].clear()
       dessiner_un_seul_anneau(Q[len(Q)-1],x2,len(Q)-1,extra)
       turtle.update()
   T[Q[len(Q)-1]].clear()
   dessiner_un_seul_anneau(Q[len(Q)-1],x2,len(Q)-1)
   turtle.update()
   return

#déplacer les anneaux de X à Z
def tour_de_Hanoi(X,Y,Z,n):
   if n == 1:
       move_ring(X,Z)
       return
   tour_de_Hanoi(X,Z,Y,n-1)
   move_ring(X,Z)
   tour_de_Hanoi(Y,X,Z,n-1)

dessiner_une_scène()
turtle.update()
n = int(turtle.numinput("Nombre d’anneau","Veuillez saisir le nombre d’anneaux:",3,2,5))
initialiser()
dessiner_des_anneaux()
tour_de_Hanoi("A","B","C",n)
turtle.update()
turtle.mainloop()