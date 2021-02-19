# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:10:03 2020

@author: Cati
"""

from Capacity import Capacity
from Power import Power
from Rules import Rules
from Temperature import Temperature

class Repository:
    def __init__(self):
        self.temperatures = Temperature().getAllTemp()
        self.powers = Power().getAllPowers()
        self.capacities = Capacity().getAllCapacities()
        self.rules = Rules().getRules()
