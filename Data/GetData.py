# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:18:36 2018

@author: matthew.cliffe
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:09:47 2018

@author: mattj
"""
from datetime import datetime
import matplotlib.pyplot as plt
import time
import serial
from time import sleep
import numpy as np

if 'ser' in locals():
    if ser.isOpen() == True:
        ser.close()
        
ser=serial.Serial(port='COM18',baudrate=9600,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
alpha1= a1
alpha2 = a2
sfr1 = []
sfr2 = []
pmr1= []
pmr2 = []
dt=[]
V=[]
fname='AlphasenseData_26072018_3.csv'

csv = open(fname,'w')
headers = 'DateTime ,' + 'Fan Voltage ,'+'SFR1 ,'+'PMr1 ,'+'SFR2 ,'+'PMr2\n'
csv.write(headers)
csv.close()
Vset=2
for lmn in np.linspace(0,1000-1,1000):
    lmn=int(lmn)
   
    data1 = alpha1.histogram()
    if type(data1) == dict:
        sfr1.append(data1.get("SFR",))
        pmr1.append(data1.get("PM10",))
    else:
        sfr1.append(0)
        pmr1.append(0)
    
    ser.write(b'VOUT1?')
    time.sleep(1)
    V.append(float(ser.read(5)))
   # print(lmn)
    
    if np.mod(lmn,50)==0:
        if Vset <= 10:
            setstr = 'VSET1:' + str(Vset+0.25)
    
            ser.write(str.encode(setstr))
            time.sleep(5)   
            ser.write(b'VOUT1?')
            time.sleep(1)
            print(float(ser.read(5)))
            Vset = Vset+0.25
    if np.mod(lmn,10)==0:
        if Vset == 10:
            setstr = 'VSET1:' + str(2)
    
            ser.write(str.encode(setstr))
            time.sleep(5)   
            ser.write(b'VOUT1?')
            time.sleep(1)
            print(float(ser.read(5)))
            Vset = 2
            
        
    data2 = alpha2.histogram()
    if type(data2) == dict:
        sfr2.append(data2.get("SFR",))
        pmr2.append(data2.get("PM10",))
    else:
        sfr2.append(0)
        pmr2.append(0)
    
    dt.append(datetime.now())

    csv=open(fname,'a')
    datawrite = dt[lmn].strftime("%Y/%m/%d %H:%M:%S")+ ' , '+ str(V[lmn])+ ' , '+str(sfr1[lmn]) +' , '+ str(pmr1[lmn])+' , '+str(sfr2[lmn])+' , '+str(pmr2[lmn]) +' ,\n'
    csv.write(datawrite)
    
    
    csv.close()

    if 1 == 2 : 
        plt.figure(1)
        plt.subplot(311)
        plt.cla()
        plt.plot(dt,pmr1,'r')
        plt.plot(dt,pmr2,'k')
        plt.subplot(312)
        plt.cla()
        plt.plot(dt,sfr1,'r')
        plt.plot(dt,sfr2,'k')
        plt.subplot(313)
        plt.cla()
        plt.plot(dt,V,'r')
        plt.pause(0.001)
        plt.draw()
        plt.show()
        
        time.sleep(0.1)
