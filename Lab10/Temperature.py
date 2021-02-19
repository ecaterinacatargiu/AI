# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:55:50 2020

@author: Cati
"""


def functionTrapez(x, boundary):
    [a, b, c, d] = boundary
    if x <= a:
        return 0
    if a <= x <= b:
        return (x-a) / (b-a)
    if b <= x <= c:
        return 1
    if c <= x <= d:
        return (d-x) / (d-c)
    if x >= d:
        return 0
    
    
    
def functionTriunghi(x, boundary):
    [a, b, c] = boundary
    if x <= a:
        return 0
    if a <= x <= b:
        return (x-a)/(b-a)
    if b <= x <= c:
        return (c-x)/(c-b)
    if x>=c:
        return 0
    
    
    
class Temperature:
    def __init__(self):
        self.cold = ("cold", [0, 15, 30, 50], functionTrapez)
        self.cool = ("cool", [30, 50, 70], functionTriunghi)
        self.moderate = ("moderate", [60, 70, 80], functionTriunghi)
        self.hot = ("hot", [70, 90, 110], functionTriunghi)
        self.veryhot = ("very hot", [90, 110, 130, 150], functionTrapez)
        
        
    def getAllTemp(self):
        return [self.cold, self.cool, self.moderate, self.hot, self.veryhot]
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    