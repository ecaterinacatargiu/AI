# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:40:52 2020

@author: Cati
"""


import numpy
from random import randint, random

'''generate a matrix - the individ '''
def generateMatrix(n):
    matrix = []
    for i in range(n):
        line = []
        for j in range(n):
            line.append((randint(1,n),randint(1,n)))
        matrix.append(line)
        
    return matrix


    
                

    
a = generateMatrix(3)
print(a)

c = [0 for x in range(3)]
print(c)

#b = checkOnColumnsI(a)
#listt = [1,2,3,4,3]
#indices = [i for i, x in enumerate(listt) if x == 3]
#print(indices)
        



 
            
            