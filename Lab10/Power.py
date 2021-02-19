# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:04:48 2020

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
    
class Power:
    def __init__(self):
        self.small = ("small", [0, 0, 10], functionTriunghi)
        self.medium = ("medium", [5, 10, 15], functionTriunghi)
        self.high = ("high", [10, 20, 20], functionTriunghi)
        
    def getAllPowers(self):
        return [self.small, self.medium, self.high]