# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:55:58 2020

@author: Cati
"""

#The repository only reads the data from database and puts each row into a list so we can treat each case individually

class Repository:
    def __init__(self):
        self.info = []
        self.readFromFile()

    def readFromFile(self):
        file = open("database.txt")
        for line in file:
            numbers = line.split(" ")
            nr = [[],[],[],[],[],[]]
            for i in range(len(numbers)):
                nr[i] = float(numbers[i])
            self.info.append(nr)
            
            
            
#r = Repository()
#print(r.info)