# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:00:09 2020

@author: Cati
"""

import math
from random import randint
from random import seed



#First we generate the table
def generateTable(n):
    p=[[0 for x in range(0,n)]for x in range(0,n)]
    return p


#check if the number is on that given row
def checkRow(table,row, value):
    
    for number in table[row]:
        if value == number:
            return True
        else:
            return False
                
#check if that number is on that given column
def checkColumn(table, column, value):
    for number in table[column]:
        if value == number:
            return True
        else:
            return False
        
#check if it was used before
def usedBefore(board, row, column, value):
    n = int(math.sqrt(len(board)))
    upperLeftCorner = (row - row % n, column - column % n)
    for row in range(upperLeftCorner[0], upperLeftCorner[0] + n):
        for col in range(upperLeftCorner[1], upperLeftCorner[1] + n):
            if board[row][col] == value:
                return True
    return False
        
    
#checks if the constrains are ok
def checkConstraints(table, row, column, value):
    return not usedBefore(table, row, column, value) and not checkRow(table, row, value) and not checkColumn(table, column, value)

#find the next free cell
def moveToNextCell(table):
    for row in table:
        for value in row:
            if value == 0:
                roww = table.index(row)
                columnn = row.index(value)
                return roww, columnn
    return -1, -1

#get a solution
def solveSudoku(table, solution):
    nextFreeCell = moveToNextCell(table)
    if nextFreeCell == [-1][-1]:
        solution.append(table)
    n = len(table)
    for number in range(1, n+1):
        if checkConstraints(table, nextFreeCell[0], nextFreeCell[1], number):
            table[nextFreeCell[0]][nextFreeCell[1]] = number
            
#print the table
            
        




def main():
    print("SUDOKU TIMEEEEE")
    print()
    print("How larger do you want your sudoku table to be? Type a n: ")
    n = int(input())
    while True:
        table = generateTable(n)
        print("Number of trials: ")
        trials = int(input())
        while trials>=0:
            trialsBefore = trials
            print(trialsBefore)
            print(table)
            solveSudoku(table, [])
            print(trials)
            print("left")
            trials = trials - 1
            trialsAfter = trials
            print(trialsAfter)
            if trials == 0:
                break
        
    


main()
    



def ranGen(n):
    return random.randrange(1,n,1)


def fillBox(row, column):
    for i in range(0,math.sqrt(n)):
        for j in range(0, math.sqrt(n)):
            number = ranGen(n)
            print(number)
        #while unUsedBox(i,j,number)==0:
           # mat[row+i][column+j] = number
            
    
    
    
            
#generateTable(4)