import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sys                                          #for path to external scripts
sys.path.insert(0,'/sdcard/FWC/module-1/trunk/matrices/CoordGeo')         #path to my scripts
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen                                                       
import subprocess  
import shlex

#Input parameters
A=np.array([2,1])
b=4.5
c=-6
M=np.array(([1,-1]))
o=0
e1=np.array(([1,0]))
O=np.array([0,0])
P = np.array([1.5,1.5])
Q = np.array([-2,-2])

D=abs(b/c)
print("ratio=",D)
omat=np.array(([0,1],[-1,0]))

#Direction vectors
m1=omat@A
m2=omat@A
m3=omat@M

#Points on the lines
x1=b/(A@e1)
A1=x1*e1
x2=c/(A@e1)
A2=x2*e1
x3=o/(M@e1)
B1=x3*e1

#Generating all lines
k1=-2
k2=2

x_AB = line_dir_pt(m1,A1,k1,k2)
x_CD = line_dir_pt(m2,A2,k1,k2)
x_EF = line_dir_pt(m3,B1,k1,k2)

#Plotting line
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_EF[0,:],x_EF[1,:])

#Labelling the coordinates 
tri_coords = np.vstack((O,P,Q)).T

#tri_coords=x.T

plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','P','Q']     
for i, txt in enumerate(vert_labels):
    plt.annotate(txt,
            (tri_coords[0,i],tri_coords[1,i]),
            textcoords="offset points",
            xytext=(0,10),
            ha='center')

plt.xlabel('$x$')
plt.ylabel('$y$')

plt.grid()
plt.axis('equal')

#for termux
plt.savefig('/sdcard/FWC/module-1/trunk/matrices/line_assignment/line.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/fwc/Divya/line.pdf"))
#else
#plt.show()
