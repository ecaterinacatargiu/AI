# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:54:17 2020

@author: Cati
"""
from random import randrange
from itertools import zip_longest
    
def generateNumbers(n):
    #randomnly generate n letters
    hexes = []
    for i in range(0,n):
        a = hex(randrange(15)).replace("0x","")
        if a == '0':
            a = hex(randrange(15)).replace("0x","")          
            b = hex(randrange(15)).replace("0x","")
            hexes.append(a+b)
          
        else:
            b = hex(randrange(15)).replace("0x","")
            hexes.append(a+b)
    return hexes
    print(hexes)
    
def toHexa(hexa):
    for i in range(0, len(hexa)):
        hexa[i] = int(hexa[i], 16)
    return hexa
        

def addLists(*iterables):
    iterables = (reversed(it) for it in iterables)
    return list(reversed([a+b for a, b in zip_longest(*iterables, fillvalue=0)]))


def subLists(*iterables):
    iterables = (reversed(it) for it in iterables)
    return list(reversed([a-b for a, b in zip_longest(*iterables, fillvalue=0)]))

def mulLists(*iterables):
    iterables = (reversed(it) for it in iterables)
    return list(reversed([a*b for a, b in zip_longest(*iterables, fillvalue=0)]))

def divLists(*iterables):
    iterables = (reversed(it) for it in iterables)
    return list(reversed([a*b for a, b in zip_longest(*iterables, fillvalue=0)]))

        
def mainCrypto():
    print("Crypto timeee")
    print("How many words do you want? ")
    mainArray = []
    nrWords = int(input())
    print(nrWords)
    while nrWords > 0:
        print("How many letters do you want the word to have?")
        lenghtWord = int(input())
        nameArray = "arr"+str(nrWords+1)
        print(nameArray)
        arr = generateNumbers(lenghtWord)
        print(arr)
        arrHexa = toHexa(arr)
        mainArray.append(arrHexa)
        print(mainArray)
        
        nrWords = nrWords - 1

    print("What kind of operation do you want?")
    op = input()
    if op == "+":
        print("addition")
        result = addLists(mainArray[0], mainArray[1])
        print(result)
    else:
        if op == "-":
            print("substraction")
            result = subLists(mainArray[0], mainArray[1])
            print(result)
        else:
            if op == "*":
                print("multiplication")
                result = mulLists(mainArray[0], mainArray[1])
                print(result)
            else:
                if op == "//":
                    print("division")
                    result = divLists(mainArray[0], mainArray[1])
                    print(result)
                    
    print("How many attempts do you want to have? ")
    trials = int(input())
    while trials > 0:
        arrT = generateNumbers(len(result))
        arrTHexa = toHexa(arrT)
        print(arrTHexa)
        for i in range(0, len(arrT)):
            if(arrTHexa[i] == result[i]):
                print("Yesss")
            else:
                print("Nope")
            
        
        trials = trials - 1
    
    
mainCrypto()





    
    

    
    
    
    
    
    
