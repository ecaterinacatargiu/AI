# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:35:10 2020

@author: Cati
"""
from Repository import Repository
from Controller import Controller
from UI import UI
from Graph import Graph

def getGraph():
    Graph()

if __name__ == '__main__':
    r = Repository()
    c = Controller(r)
    ui = UI(c)
    x = threading.Thread(target = getGraph)
    x.start()
    ui.run()