# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:15:46 2020

@author: Cati
"""

from Controller import Controller
from Repository import Repository
from Graph import Graph

class UI:
    def __init__(self, c: Controller):
        self.controller = c

    def run(self):
        while True:
            temperature = float(input("Temperature(20-120): "))
            capacity = float(input("Capacity(0-10): "))
            self.controller.runAlg(temperature, capacity)
            
            
            

