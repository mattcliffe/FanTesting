# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:16:09 2018

@author: matthew.cliffe
"""

from usbiss.spi import SPI
import opc

p1 = 'COM19'
spi1=SPI(p1)
spi1.mode = 1
spi1.max_speed_hz = 30000
a1=opc.OPCN2(spi1)
a1.on()


p2 = 'COM20'
spi2=SPI(p2)
spi2.mode = 1
spi2.max_speed_hz = 30000
a2=opc.OPCN2(spi2)
a2.on()

