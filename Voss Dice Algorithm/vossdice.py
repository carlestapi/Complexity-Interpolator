#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:36:09 2019

Algoritmo de Voss para ruido rosa utilizando 8 dados

@author: carlestapi
"""

import numpy as np
import matplotlib.pyplot as plt

midiC3=48

from random import randint


numDice,biasDie,listDice,listPink=8,3.5,[0,0,0,0,0,0,0,0],[midiC3]

tonalInt,indexRange=[-12,-10,-8,-5,-3,-1,0,2,4,5,7,9,11,12],9900

def rollDie():
    return randint(1,6)-biasDie




def voss(index): #establecer que dado tirar
    listDice[0]=rollDie()
    if index%2==0:listDice[1]=rollDie()
    if index%4==0:listDice[2]=rollDie()
    if index%8==0:listDice[3]=rollDie()
    if index%16==0:listDice[4]=rollDie()
    if index%32==0:listDice[5]=rollDie()
    if index%64==0:listDice[6]=rollDie()
    if index%128==0:listDice[7]=rollDie()
    return listDice



def pinkNoise(listPink): 
    pink=0

#mapeo sobre el numero requerido de notas
    
    for index in range (indexRange):
        pink=int(sum(voss(index)))
        
        while pink not in tonalInt: #filtrar intervalos no tonales
            pink=int(sum(voss(index)))
        listPink.append(pink+midiC3)    
    listPink.append(midiC3)
    return listPink

print(pinkNoise(listPink))
plt.plot(listPink,'bo')
plt.show()
            
            