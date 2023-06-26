import pyttsx3
hello = []
hellow = 'hello world'
hello.append(hellow)

from sympy import *
x = Symbol('x')

class Segments:
    def __init__(self, distance):
        self.distance = distance

    def length(self):
        return self.distance

def rule34_5(x, y, z):
    if x > 0:
        a = x/3
    elif y > 0:
        a = y/4
    else:
        a = z/5
    
    sol = [3*a, 4*a, 5*a]

    return sol


AE = Segments(16)
AF = Segments(12)
EF = Segments(rule34_5(AF.length(), AE.length(), 0)[2])
FO = Segments(EF.length() / 2)
MO = Segments(rule34_5(0, 0, FO.length())[1])
FM = Segments(rule34_5(0, MO.length(), FO.length())[0])
NO = Segments(FO.length())
OP = Segments(FM.length())
AB = Segments(MO.length() + NO.length())
AD = Segments(OP.length() + FO.length())

diameter = sqrt(16**2 + 12**2)
radius = diameter/2
area = pi * radius**2
area_semi_circle = area/2
area_triangle = 16*12/2

area_rectangle = AB.length() * AD.length()

area_zone = area_rectangle - area_semi_circle - area_triangle

from matplotlib.patches import *
import matplotlib.pyplot as plt
import numpy as np
from numpy import *

fig = plt.figure()
plt.xlim(0,20)
plt.ylim(0,20)
someX, someY = 1, 1
currentAxis = plt.gca()
currentAxis.add_patch(Rectangle((someX, someY), 18, 16,
                    facecolor = "green", ec = 'k', linewidth = 2))

plt.plot(9, 7, "black", marker = 'o')
plt.gca().annotate('O', xy = (9 + 0.2, 7 + 0.2),
                xycoords = 'data', fontsize = 10)

angles = linspace(-0.205 * pi, 0.796 * pi, 100)
r = 10
xs = r * cos(angles) + 9
ys = r * sin(angles) + 7
plt.plot(xs, ys, color = 'red')
plt.fill(xs, ys, "white")

plt.plot([1, 17], [13, 1], color = "blue", linewidth = 2)

plt.fill("j", "k", 'w',
         data = {"j": [1.04, 1, 17], "k":[1.04, 13, 1]})

plt.gca().set_aspect('equal')
plt.show()


engine = pyttsx3.init()
engine.setProperty('rate', 250)
engine.say(hello)
z = ["world"]
engine.say(z)
y = hello + z
engine.runAndWait()