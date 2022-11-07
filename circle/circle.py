
#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys                #for path to external scripts
import sympy as sym
from sympy import symbols

sys.path.insert(0,'/sdcard/FWC/module-1/trunk/matrices/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters
r1 = 1     #radius   #distance of points from center
u1 = np.array(([1,1]))   #center
r2 = symbols('r') #radius
u2 = np.array(([0,r2]))  #center
c=u1-u2
d=c@c
exp=(1+r2)**2
g=sym.solve(d-exp,r2)
r2=g
print(g)
n=float(g[0])
u2 = np.array(([0,n]))
e1 = np.array(([1,0]))

#Generating the circle
x_circ1= circ_gen(u1,r1)
x_circ2= circ_gen(u2,n)
x_u1u2 = line_gen(u1,u2)
#
#
#Plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='Circle - C')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='Circle - T')
plt.plot(x_u1u2[0,:],x_u1u2[1,:],label='1+r2')

#Labeling the coordinates
tri_coords = np.vstack((u1,u2)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['u1(1,1)','u2(0,y)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]),
                 # this is the point to label
                 textcoords="offset points",
                 # how to position the text
                 xytext=(-5,10),
                 # distance from text to points (x,y)
                 ha='center')
    # horizontal alignment can be left, right or center

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/FWC/module-1/trunk/matrices/circle/circle1.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/matrices/Circle/circle1.pdf'"))
#else
#plt.show()

