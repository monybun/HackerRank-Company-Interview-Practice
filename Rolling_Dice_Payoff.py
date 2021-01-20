#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rolling Dices Payoff Optimization Fuction: One Dice
-----------------------------------------------------------------------------------------------------------------
from 1 roll: the rolling outcome will be 1,2,3,4,5,6 -->expected value = 3.5

from 2 rolls: if the 1st roll outcome is 4,5,6 (above 3.5), stop rolling ---> in virtue of optimization
                      the chance of starting the 2nd roll is then 0.5
                      The mean of 4,5,6 is 5, the expected payoff of my 2nd roll is 3.5
                      total payoff = 0.5*3.5 + 0.5*5 = 4.25
                      
from 3 rolls: the expected avg payoff now is 4.25, if 1st roll turns out to be 5 or 6 ---> stop rolling
                      expected payoff from 5,6 is 5.5
                      by rerolling--->back to a 2 roll game ---> expected payoff 4.25
                      total expected payoff = (1/3)*5.5 + (2/3)*4.25 = 4.66
        .
        .
        .
from i rolls: a recursive function
-----------------------------------------------------------------------------------------------------------------
"""
import numpy as np

def Ex_Payoff_Rolls(i):
    if i == 1: 
        res = np.mean(range(1,7))
    else:
        reroll_probability = int(Ex_Payoff_Rolls(i-1)) / 6
        Ex_Payoff_No_reroll = np.mean(range(int(Ex_Payoff_Rolls(i-1)) + 1, 7))
        res = reroll_probability*Ex_Payoff_Rolls(i-1) + (1-reroll_probability)*Ex_Payoff_No_reroll
    return res
    
print(Ex_Payoff_Rolls(1))
print(Ex_Payoff_Rolls(2))
print(Ex_Payoff_Rolls(3))
print(Ex_Payoff_Rolls(4))
print(Ex_Payoff_Rolls(5))
print(Ex_Payoff_Rolls(6))
print(Ex_Payoff_Rolls(7))
print(Ex_Payoff_Rolls(8))
print(Ex_Payoff_Rolls(9))
