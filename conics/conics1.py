import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from sympy import symbols, Eq, solve 
import math
#for equations
import sys      
import sympy as sym
from sympy import Poly,roots,simplify
sys.path.insert(0,'/sdcard/FWC/module-1/trunk/matrices/CoordGeo')
#/sdcard/FWC/module-1/trunk/matrices/conics
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using 
import subprocess
import shlex
#end if
#
#line
A=np.array(([2,np.sqrt(6)]))
B=np.array(([2]))
e1=np.array(([1,0]))
n = A
c = B
m1=omat@n

x1=c/(n@e1)
q2=x1*e1
k1=-8
k2=8
x_AB=line_dir_pt(m1,q2,k1,k2)
plt.plot(x_AB[0,:],x_AB[1,:])

def hyper_gen(y):
    x= np.sqrt(4+2*y**2)
    return x
#
len = 10
y = np.linspace(-10,len)
x = hyper_gen(y)
plt.axhline(y=0,color='black')
plt.axvline(x=0,color= 'black')
#plotting the hyperbola
plt.plot(x,y,label='Hyperbola')
plt.plot(-x,y)
#
V = np.array(([1,0],[0,-2]))
u = np.array(([0,0]))
m2 = np.array(([-np.sqrt(6),2]))
f = -4

K1 = ( - m2.T@(V@q2 + u))/(m2.T@V@m2)
c = q2 + K1*m2
#a1 = q2 + K2*m2
print(c)
tri_coords = np.vstack((q2,c)).T
plt.scatter(tri_coords[0,:],tri_coords[1,:])
vert_labels = ['q(1,0)','c(4,-√6)']
for i, txt in enumerate(vert_labels):
     plt.annotate(txt, # this is the text
                   (tri_coords[0,i],tri_coords[1,i]), # this is the point to label
                   textcoords="offset points", # how to position the text
                   xytext=(25  ,-2), # distance from text to points (x,y)
                   ha='center') # horizontal alignment can be left, right or center

#
#
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
#plt.xlim(-5,10)
#plt.ylim(-5,10)

#for termux 
#/sdcard/FWC/module-1/trunk/matrices/conics  
plt.savefig('/sdcard/FWC/module-1/trunk/matrices/conics/conics11.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/FWC/module-1/trunk/matrices/conics/conics11.pdf'"))
#else
#plt.show()
