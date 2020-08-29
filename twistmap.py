import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const
import sys
import os
import imageio


print(sys.getrecursionlimit())



length = 10000 
points = np.zeros((2,length))

if (length >= 996):
    sys.setrecursionlimit(length+4)
print(sys.getrecursionlimit())


#set f = g 
#=> d/dr f = - d/dphi f

def f(r,phi):
    return np.sin(phi - r)

def g(r,phi):
    return np.sin(phi - r)

def twistMap(r, phi,windingnumber,perturbation,counter):
    if (counter < length):
        points[0][counter] = r + perturbation*f(r,phi)
        points[1][counter] = phi+2*np.pi*windingnumber + perturbation*g(r,phi)
        return twistMap(r+ perturbation*f(r,phi) , phi+2*np.pi*windingnumber + perturbation*g(r,phi),windingnumber, perturbation,counter+1)



#x = r*cos(phi)
#y = r*sin(phi)



def createPlot(initvalues, windingnumber, perturbation):
    

    twistMap(initvalues[0],initvalues[1], windingnumber, perturbation,  0)
    x = points[0][:]*np.cos(points[1][:])
    y = points[0][:]*np.sin(points[1][:])
    plt.scatter(x,y, label=str(windingnumber))

currentdir =  os.path.dirname(os.path.realpath(__file__))
files = []
for i in range(1,100,1):
    perturbation = i/100

    createPlot((1,0), const.golden, perturbation)
    createPlot((0.5,0), const.pi, perturbation)
    createPlot((0.7,0), 1/4, perturbation)

    plt.axis('scaled')
    #plt.legend()
    plt.title(str(perturbation))
    name = str(currentdir) +str("/images/") + str(perturbation) + str('.png')
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.savefig(name, dpi=200)
    plt.clf()
    files.append(name)



images = [imageio.imread(file) for file in files]
imageio.mimwrite(str(currentdir) + '/animation.gif', images, fps=10)