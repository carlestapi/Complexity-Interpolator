#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 13:45:08 2019

@author: carlestapi
"""

from __future__ import print_function, division

import thinkdsp
import thinkplot
import numpy as np
import pandas as pd
import scipy.signal
import math
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

wave = thinkdsp.read_wave('interp.wav')
wave.normalize()
wave.make_audio()
spectrum = wave.make_spectrum()

wave2 = thinkdsp.read_wave('1sine.wav')
wave.normalize()
wave.make_audio()
spectrum2 = wave2.make_spectrum()

wave3 = thinkdsp.read_wave('2PinkNoise.wav')
wave.normalize()
wave.make_audio()
spectrum3 = wave3.make_spectrum()

slopeINT = spectrum.estimate_slope().slope
print(slopeINT)

spectrum.plot_power(linewidth=0.5,color='#c4483d',label=('Interpolation Sine x 1/f - beta', slopeINT))
thinkplot.config(xlabel='frequency (Hz)',
                 ylabel='power',
                 xscale='log',
                 yscale='log',
                 xlim=[0, spectrum.fs[-1]],
                 legend='TRUE')

spectrum2.plot_power(linewidth=0.95,label='Sine')
thinkplot.config(xlabel='frequency (Hz)',
                 ylabel='power',
                 xscale='log',
                 yscale='log',
                 xlim=[0, spectrum.fs[-1]],
                 legend='TRUE')

spectrum3.plot_power(linewidth=0.95,color='#addbb5',label='1/f')
thinkplot.config(xlabel='frequency (Hz)',
                 ylabel='power',
                 xscale='log',
                 yscale='log',
                 xlim=[0, spectrum3.fs[-1]],
                 legend='TRUE')

