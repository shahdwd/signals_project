# -*- coding: utf-8 -*-
"""
Created on Thu May 11 21:21:05 2023

@author: shwae
"""


import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd



C3 = 130.81 
D3 = 146.83
E3 = 164.81
F3 = 174.61
G3 = 196
A3 = 220
B3 = 246.93

C4 = 130.81*2
D4 = 146.83*2
E4 = 164.81*2
F4 = 174.61*2
G4 = 196*2
A4 = 220*2
B4 = 246.93*2




𝑡 = np.linspace(0,3,12*1024)

F_array = np.array([C3*2,D3*2,E3*2,F3*3,G3*4,A3*5,B3*6])
f_array = np.array([C4,D4*2,E4,F4*4,G4,A4*4,B4])


t_array = np.array([ 0, 1.2, 1.4, 1.6, 2.3, 3, 3.5, 3.1])
T_array = np.array([0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.3]) 

N=7
j=0
i=0
x=0
while (i<N):
    Fi = F_array[i]
    fi = f_array[i]
    ti = t_array[i]
    Ti = T_array[i]
    Notei = np.sin(2*np.pi*Fi*t)
    notei = np.sin(2*np.pi*fi*t)
    x = x + (Notei+notei)*((t>=ti)&(t<=(ti+Ti)))
    i = i+1
    
plt.plot(t,x)
sd.play(x,3*1024)

    


