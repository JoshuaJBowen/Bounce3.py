#Bounce3 (add Vectors)
#Josh Bowen
#5/3/2022

import turtle
import random
import math

class Ball():

    def __init__(self, name, color):
        self.name = name
        theta = random.randrange(0,200)
        theta = theta*math.pi/100
        self.op = [0,0]
        self.v = [math.cos(theta), math.sin(theta)]
        self.t = 0
        self.intercept = [0,0]
        
        self.name = turtle.Turtle()
        #self.name.up()
        self.name.color(color)
        self.name.speed(0)#0)
        self.name.shape("circle")

    def solve(self):
        possible_t = [0,0,0,0]
        if (200 - self.op[0])/self.v[0] > 0:
            possible_t[0] = (200 - self.op[0])/self.v[0]
        else:
            possible_t[0] = 1000
        if (-200 - self.op[0])/self.v[0] > 0:
            possible_t[1] = (-200 - self.op[0])/self.v[0]
        else:
            possible_t[1] = 1000
        if (200 - self.op[1])/self.v[1] > 0:
            possible_t[2] = (200 - self.op[1])/self.v[1]
        else:
            possible_t[2] = 1000
        if (-200 - self.op[1])/self.v[1] > 0:
            possible_t[3] = (-200 - self.op[1])/self.v[1]
        else:
            possible_t[3] = 1000
        self.t = min(possible_t)
            
    def bounce(self):
        self.intercept = [int(self.op[0] + self.v[0]*self.t), int(self.op[1] + self.v[1]*self.t)]
        self.name.goto(self.intercept)
        self.op = self.intercept #self.op holds the last intercept
        
        if abs(self.intercept[0]) == 200:
            self.v[0] = -1*self.v[0]
        if abs(self.intercept[1]) == 200:
            self.v[1] = -1*self.v[1]
            
        self.t = 0
            
    def inside(self):
        if self.op[0] >= -200 and self.op[0] <= 200 and self.op[1] >= -200 and self.op[1] <= 200:
            return True
        else:
            return False
            
def main():
    
    wn = turtle.Screen()
    wn.bgcolor("Black")
        
    bound = turtle.Turtle()
    bound.color("White")
    bound.speed(0)
    bound.width(5)
    bound.ht()
    bound.up()
    bound.goto(-210, -210)
    bound.down()
    bound.goto(210, -210)
    bound.goto(210, 210)
    bound.goto(-210, 210)
    bound.goto(-210, -210)

    my_ball = Ball("tennis", "lightblue")
    
    while my_ball.inside():
            my_ball.solve()
            my_ball.bounce()

main()

#--------------------------
#Goals for future versions:
#Make it gereralized to vector walls to bounce off of not constants
#What if we could make this generalized to any shape
#what if we made balls able to bounce off each other
#---------------------
