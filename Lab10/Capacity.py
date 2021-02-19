# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:08:01 2020

@author: Cati
"""


def functionTriunghi(x, boundary):
    [a, b, c] = boundary
    if x <= a:
        return 0
    if a <= x <= b:
        return (x - a) / (b - a)
    if b <= x <= c:
        return (c - x) / (c - b)
    if x >= c:
        return 0
    
    
class Capacity:
    def __init__(self):
        self.small = ("small", [0,0,5], functionTriunghi)
        self.medium = ("medium", [3,5,7], functionTriunghi)
        self.high = ("high",[5,10,10], functionTriunghi)
        
    def getAllCapacities(self):
        return [self.small, self.medium, self.high]