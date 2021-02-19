# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:53:41 2020

@author: Cati
"""

from Ant import Ant
from Problem import Problem

from Controller import Controller


class UI:
    
    def __init__(self, controller: Controller):
        self.controller = controller
        
        
    def run(self):
        (fitness, solution) = self.controller.run()
        print()
        print(fitness)
        for line in solution:
            print(line)
            
            

p = Problem()
p.loadProblem()
c = Controller()
c.loadParams(p)
ui = UI(c)
ui.run()

        
        
    