#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 23:36:09 2019

Algoritmo de Voss para ruido rosa utilizando 8 dados - TO MIDI

@author: carlestapi
"""

import numpy as np
import matplotlib.pyplot as plt

midiC3=48

from random import randint


numDice,biasDie,listDice,listPink=8,3.5,[0,0,0,0,0,0,0,0],[midiC3]

tonalInt,indexRange=[-12,-10,-8,-5,-3,-1,0,2,4,5,7,9,11,12],25

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

from miditime.miditime import MIDITime

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
mymidi = MIDITime(120, 'simple.mid')

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
#midinotes = [
#    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
#    [10, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
#]

#midinotes = [
#        [0,48,127,1],
#        [1,48,127,1],
#        [2,48,127,1],
#        [3,48,127,1],
#        [4,48,127,1],
#        [5,48,127,1],
#        [6,48,127,1],
#        [7,48,127,1],
#        [8,48,127,1],
#        [9,48,127,1],
#        [10,48,127,1],
#        [11,48,127,1],
#        [12,48,127,1],
#        [13,48,127,1],
#        [14,48,127,1],
#        [15,48,127,1],
#        [16,48,127,1],
#        [17,48,127,1],
#        [18,48,127,1],
#        [19,48,127,1],
#        [20,48,127,1],
#        [21,48,127,1],
#        [22,48,127,1],
#        [23,48,127,1],
#        [24,48,127,1],
#        [25,48,127,1],
#        ]

# Add a track with those notes
mymidi.add_track(midinotes)

# Output the .mid file
mymidi.save_midi()
