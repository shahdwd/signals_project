# -*- coding: utf-8 -*-
"""
Created on Sat May 20 19:51:41 2023

@author: shwae
"""


import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import math



𝑡 = np.linspace(0,3,12*1024)

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


F_array = np.array([C3*2,D3*2,E3*2,F3*3,G3*4,A3*5,B3*6])
f_array = np.array([C4,D4*2,E4,F4*4,G4,A4*4,B4])


t_array = np.array([ 0, 1.2, 1.4, 1.6, 2.3, 3, 3.5, 3.1])
T_array = np.array([0.3, 0.1, 0.1, 0.1, 0.3, 0.1, 0.1, 0.3]) 

N=7
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

#plt.plot(t,x)
#sd.play(x,3*1024)



N = 3*1024
f = np. linspace(0 , 512 , int(N/2))


x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])


fn1 , fn2 = np. random. randint(0, 512, 2)
n = np.sin(2*np.pi*fn1*t)+np.sin(2*np.pi*fn2*t)


xn = x+n
xn_f = fft(xn)
xn_f = 2/N * np.abs(xn_f [0:np.int(N/2)])


z = np.where(xn_f>math.ceil(np.max(x)))
index1 = z[0][0]
index2 = z[0][1]


found1 = int(f[index1])
found2 = int(f[index2])


xFiltered = xn - (np.sin(2*np.pi*found1*t)+np.sin(2*np.pi*found2*t))


sd.play(xFiltered, 3*1024)


xFiltered_f = fft(xFiltered)
xFiltered_f = 2/N * np.abs(xFiltered_f [0:np.int(N/2)])


plt.figure()
plt.subplot(3,1,1)
plt.plot(t,x)
plt.subplot(3,1,2)
plt.plot(t,xn)
plt.subplot(3,1,3)
plt.plot(t,xFiltered)


plt.figure()
plt.subplot(3,1,1)
plt.plot(f,x_f)
plt.subplot(3,1,2)
plt.plot(f,xn_f)
plt.subplot(3,1,3)
plt.plot(f,xFiltered_f)
