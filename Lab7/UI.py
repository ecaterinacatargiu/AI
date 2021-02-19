# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:56:32 2020

@author: Cati
"""
from Repository import Repository
from Controller import Controller

class UI:
    
    def __init__(self, controller:Controller):
        self.controller = controller
        
    def start(self):
        while True:
            iterations = int(input("Please input the number of iterations: "))
            learnRate = float(input("Please input the learning rate: "))
            self.controller.setAttributes(iterations, learnRate)
            self.controller.run()


repository = Repository()
ctrl = Controller(repository)
ui = UI(ctrl)
ui.start()