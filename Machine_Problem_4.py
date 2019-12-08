# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:29:24 2019

@author: Wency
"""

from matplotlib import pyplot as plt
import math 

def Projection(S,V,angle,AX,AY):
     
    if AY== 0:
        print("Error: Vertical acceleration must not be equal to 0")
        return  
    
    x_val= [] 
    y_val= []
    
    VX= V*math.cos(angle*(3.14/180)) 
    VY= V*math.sin(angle*(3.14/180)) 
    
    x= 0
    y= S
    t= 0
    delta= 0.0001 
    
    x_val.append(x)
    y_val.append(y)
    
    while(True):
        t= t+delta
        x= VX*t + (0.5)*AX*(t*t)
        y= VY*t + (0.5)*AY*(t*t) + S
        
        x_val.append(x)
        y_val.append(y)
        
        if y < delta:
            break
        
    plt.plot(x_val,y_val)  
    ax = plt.gca()
    ax.set_ylim([0,max(y_val)])
    plt.grid()
    plt.show()
    plt.xlabel('Horizontal distance in meters')
    plt.ylabel('Vertical distance in meters')
    plt.title('Simulation of projectile motion')
    
        
if __name__ == '__main__':
   S = 0
   V = 20
   angle = 30
   AX = 20
   AY = 15
   Projection(S,V,angle,AX,AY)