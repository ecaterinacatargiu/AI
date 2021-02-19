# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:04:02 2020

@author: Cati
"""


class Rules:
    def __init__(self):
        self.rules = [("cold", "small", "small"),
                      ("cold", "medium", "medium"),
                      ("cold", "high", "high"),
                      ("cool", "small", "small"),
                      ("cool", "medium", "medium"),
                      ("cool", "high", "high"),
                      ("moderate", "small", "small"),
                      ("moderate", "medium", "small"),
                      ("moderate", "high", "small"),
                      ("hot", "small", "small"),
                      ("hot", "medium", "small"),
                      ("hot", "high", "small"),
                      ("very hot", "small", "small"),
                      ("very hot", "medium", "small"),
                      ("very hot", "high", "small")]

    def getRules(self):
        return self.rules
