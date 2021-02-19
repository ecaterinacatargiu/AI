# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:11:35 2020

@author: Cati
"""

def inverseTriangle(y, boundary):
    [a,b,c] = boundary
    return ((y*(b-a)+a) + (y * (b-c) + c)) / 2


from Repository import Repository

class Controller:
    def __init__(self, repo: Repository):
        self.repository = repo
        
    def applyRules(self, temperature, capacity):
        rules = self.repository.rules
        allTemperatures = self.repository.temperatures
        allCapacity = self.repository.capacities
        allPowers = self.repository.powers
        
        fuzzySet = []
        for (temp, cap, power) in rules:
            print("If temperature is ", temp, " and capacity is ", cap, " power is ", power )
            for (t, boundary, function) in allTemperatures:
                if t == temp:
                    resultTemperature = function(temperature, boundary)
                    break
            for (c, boundary, function) in allPowers:
                if c == cap:
                    resultCapacity = function(capacity, boundary)
                    break
            print("Membership temperature =", resultTemperature, "membership capacity = ", resultCapacity)
            powerX = min(resultCapacity, resultTemperature)
            if powerX != 0:
                for (p, boundary, function) in allPowers:
                    if power == p:
                        print(powerX, boundary, p)
                        fuzzySet.append((inverseTriangle(powerX,boundary), powerX))
                        print("Power = ", inverseTriangle(powerX, boundary), "Membership power =", powerX)
            else:
                print("Fuzzy set for this rule is null")
            print("###########################")
        return fuzzySet
    
    
    def runAlg(self, temperature, capacity):
        fuzzySet = self.applyRules(temperature, capacity)
        sum1 = 0
        sum2 = 0
        for (x, result) in fuzzySet:
            sum1 = sum1 + x * result
            sum2 = sum2 + result

        if sum2 != 0:
            print(sum1 / sum2)
        else:
            print(0)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    