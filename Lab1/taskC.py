# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 18:43:24 2020

@author: Cati
"""
from random import sample
from typing import List, Dict
import string
import operator
from copy import deepcopy
from math import sqrt
import numpy


###########################################################################

#firstly we get random hexa numbers mapped to corresponding  each letter and returning it as dictionary LETTER -> HEXA DIGIT
def getRandom(letters: List[str]) -> Dict[str, str]:
    
    digits = [str(i) for i in range(10)] + list(x for x in string.ascii_uppercase[:6])
    return {k: v for k, v in zip(letters, sample(digits, len(letters)))}
    
#hexa repr of a word
def toHex(word: str, mapping: Dict[str, str]) -> str:
    return ''.join(mapping[c] for c in word)


#solving the operation between words and returning it as a dictionary word1 operation word2 result
def solveCrypto(word1: str, word2: str, operation: str, result: str, trials: int = 100) -> Dict:
    
    #here we have  dictionary for each possible operation
    operations  = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}
    letters = list(set(word1) | set(word2) | set(result) )
    
    mapp = None
    #ok = True : fully decrypted
    ok = False
    
    while trials != 0 and not ok:
        trials = trials - 1
        mapp = getRandom(letters)
        
        hexes = [word1, word2, result]
        hexes = [''.join(mapp[x] for x in y) for y in hexes]
        
        numbers = [int(x, 16) for x in hexes]
        oper = operations[operation]
        if oper(numbers[0], numbers[1]) == numbers[2]:
            print(oper(numbers[0], numbers[1]))
            print("They are matching")
            ok = True
            break
        
        if not ok and trials == 0:
            print("Not matching")
            break
        
    return mapp

        

#############################################################################
            
    
def readSudoku(fileName):
    
    file = open(fileName, 'r')
    board = [[int(num) for num in line.split(" ")] for line in file]
    return board


def checkRow(board, row, value):
    for number in board[row]:
        if value == number:
            return True
    return False



def checkColumn(board, column, value):
    for row in board:
        if value == row[column]:
            return True
    return False


def checkBox(board, row, column, value):
    n = int(sqrt(len(board)))
    upperLeftCorner = (row - row % n, column - column % n)
    for row in range(upperLeftCorner[0], upperLeftCorner[0] + n):
        for col in range(upperLeftCorner[1], upperLeftCorner[1] + n):
            if board[row][col] == value:
                return True
    return False




def isValid(board, row, column, value):
    return not checkBox(board, row, column, value) and not checkRow(board, row, value) and not checkColumn(board, column, value)
    


def getNextFreeCell(board):
    
    for col in board:
        for value in col:
            if value == 0:
                r = board.index(col)
                print(r)
                c = col.index(value)
                print(c)
                return r,c
    return -1,-1



def solve(board, solutions):
    
    freeCell = getNextFreeCell(board)
    print(freeCell)
    if(freeCell == -1,-1):
        solutions.append(deepcopy(board))
        
    n = len(board)
    for number in range(1, n+1):
        if isValid(board, freeCell[0], freeCell[1],number):
            board[freeCell[0]][freeCell[1]] = number
            solve(board, solutions)

            
            
            
def printSol(solutions):
    if len(solutions) > 0:
        for solution in solutions:
            for row in solution:
                for value in row:
                    print(value, end=' ')
                print()
            print()
    else:
        print("No solution.")
    
    
def run():
    
    print("4x4boardsudoku-0.txt")
    board = readSudoku(r"D:\An II\Sem2\AI\4x4boardsudoku-0.txt")
    solutions = []
    solve(board, solutions)
    printSol(solutions)
    
    print("9x9boardsudoku-0.txt")
    board = readSudoku(r"D:\An II\Sem2\AI\9x9boardsudoku-0.txt")
    solutions = []
    solve(board, solutions)
    printSol(solutions)


#run()
    
    
    

##########################################################################
        

def generateMatrix(n,m):
    matrix = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(0)
        matrix.append(line)
        
    return matrix

            
def printMatrix(A): 
    N = len(A[0]) 
    for i in range(N): 
        print(A[i]) 
            

def checkInBoard(row, column):
    return 0<=row<=5 and 0<=column<=6
    

def move(board, row, column, form):
    
    for tuplu in form:
        if checkInBoard(row+tuplu[0],column+tuplu[1]):
            board[row+tuplu[0]][column+tuplu[1]] += 1
        else:
            return False
                        
    #print(board)
    return board




def isMoveValid(board):
    
    for i in range(0, 5):
        for j in range(0, 6):
            if board[i][j] > 1:
                return False
    return True

def solveGeo():
    
    board = generateMatrix(5,6)
    
    forms = [
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2)],
            [(0, 0), (1, 0), (1, 1), (1, 2)],
            [(0, 0), (0, 1), (0, 2), (1, 2)],
            [(0, 0), (0, 1), (-1, 1), (0, 2)]
            ]
    
    copyBoard = deepcopy(board)
    
    ok =1
    for i in range(5):
        randomRow = int(numpy.random.uniform(low=0, high=5))
        randomColumn = int(numpy.random.uniform(low=0, high=6))
            
        try:
            if not move(copyBoard, randomRow, randomColumn, forms[i]):
                ok = 0

        except:
            print("Nope")
                
    print(copyBoard)      
    if isMoveValid(copyBoard) and ok==1:
        print("Solution found!!:")
    else:
        print("Nope :(")
        
    return copyBoard
        

#solveGeo()

    
##########################################################################    

def main():
    print("Which problem do you want to try to solve?")
    nrProblem = int(input())
    while(1):
        if nrProblem == 1:
            print("SUDOKU TIMEEE")
            attempts = int(input("Input the number of attempts: "))
            while attempts > 0:
                solutionSudoku = run()
                print(solutionSudoku)
                attempts = attempts -  1             
        else:
            if nrProblem == 2:
                print("Crypto timeee")
                word1, word2, operation, result, attempts = [None] * 5
                word1 = input("Input the first word: ")
                word2 = input("Input the second word: ")
                operation = input("Input the desired operation: ")
                result = input("Input result: ")
                attempts = int(input("Input the numbers of attempts: "))
                while attempts > 0:
                    solutionCrypto = solveCrypto(word1, word2, operation, result, attempts)
                    print(solutionCrypto)
                    print(toHex(word1, solutionCrypto) + f' {operation} ' + toHex(word2, solutionCrypto) + ' = ' + toHex(result, solutionCrypto))
                    attempts -= 1
            else:
                if nrProblem == 3:
                    attempts = int(input("Input the numbers of attempts: "))
                    while attempts > 0:
                        print()
                        solveGeo()
                        attempts -= 1      
                    
main()