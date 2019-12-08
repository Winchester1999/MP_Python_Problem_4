import math 
import numpy as np
import matplotlib.pyplot as plt
import sys

Y= float(input('Input Initial height: '))
V= float(input('Input Initial velocity: '))
angle= float(input('Input Angle in degrees: '))
Ax= float(input('Input x-component acceleration: '))
Ay= float(input('Input y-component acceleration - should be negative: '))

if Ay >= 0:
        print('There is no freefall, the vertical acceleration should be negative.')
        sys.exit()
        
angle= math.radians(angle)
Vx= V*math.cos(angle)
Vy= V*math.sin(angle)

R= [Ay/2, Vy, Y]
M= max(np.roots(R))

r= np.arange(0,M,0.01)
x= np.zeros(len(r)+1)
y= np.zeros(len(r)+1) 
t= 0.01

x[0]= 0
y[0]= Y
p = np.arange(0,len(r)-1,1)

for o in p:
    xt= (Ax*(t**2))/2 + Vx*t
    yt= (Ay*(t**2))/2 + Vy*t + Y
    
    x[o+1]= xt
    y[o+1]= yt
    t=t+0.01
    
x[len(r)]= ((Ax/2)*M**2) + Vx*M
y[len(r)]= 0

plt.plot(x,y, color='cyan', linewidth=2)
plt.grid()
plt.xlabel ('Horizontal  Distance in meters')
plt.ylabel ('Vertical Distance in meters')
plt.title ('Projectile Motion')
