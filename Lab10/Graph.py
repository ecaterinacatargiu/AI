# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:16:52 2020

@author: Cati
"""

import matplotlib.pyplot as plt


def functionTrapezGraph(x, boundary, xValue, yValue):
    [a, b, c, d] = boundary
    xValue.append(x)
    if x <= a:
        yValue.append(0)
        return 0
    if a <= x <= b:
        yValue.append((x - a) / (b - a))
        return (x - a) / (b - a)
    if b <= x <= c:
        yValue.append(1)
        return 1
    if c <= x <= d:
        yValue.append((d - x) / (d - c))
        return (d - x) / (d - c)
    if x >= d:
        yValue.append(0)
        return 0


def functionTriangleGraph(x, boundary, xValue, yValue):
    [a, b, c] = boundary
    xValue.append(x)
    if x <= a:
        yValue.append(0)
        return 0
    if a <= x <= b:
        yValue.append((x - a) / (b - a))
        return (x - a) / (b - a)
    if b <= x <= c:
        yValue.append((c - x) / (c - b))
        return (c - x) / (c - b)
    if x >= c:
        yValue.append(0)
        return 0

class Graph:
    def __init__(self):
        self.getGraph()


    def getGraph(self):
        small = [-5, 0, 5]
        medium = [3, 5, 7]
        high = [5, 10, 15]
        x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
        for i in range(0, 11):
            functionTriangleGraph(i, small, x1, y1)
            functionTriangleGraph(i, medium, x2, y2)
            functionTriangleGraph(i, high, x3, y3)
        f1 = plt.figure("Capacity")
        plt.plot(x1, y1, label="small")
        plt.plot(x2, y2, label="medium")
        plt.plot(x3, y3, label="high")
        plt.legend(loc='center right')

        small = [-10, 0, 10]
        medium = [5, 10, 15]
        high = [10, 20, 30]
        x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
        for i in range(0, 21):
            functionTriangleGraph(i, small, x1, y1)
            functionTriangleGraph(i, medium, x2, y2)
            functionTriangleGraph(i, high, x3, y3)
        f2 = plt.figure("Power")
        plt.plot(x1, y1, label="small")
        plt.plot(x2, y2, label="medium")
        plt.plot(x3, y3, label="high")
        plt.legend(loc='center right')

        cold = [0, 15, 30, 50]
        cool = [30, 50, 70]
        moderate = [60, 70, 80]
        hot = [70, 90, 110]
        veryhot = [90, 110, 130, 150]
        x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = [], [], [], [], [], [], [], [], [], []
        for i in range(20, 121):
            functionTrapezGraph(i, cold, x1, y1)
            functionTriangleGraph(i, cool, x2, y2)
            functionTriangleGraph(i, moderate, x3, y3)
            functionTriangleGraph(i, hot, x4, y4)
            functionTrapezGraph(i, veryhot, x5, y5)
        f3 = plt.figure("Temperature")
        plt.plot(x1, y1, label="cold")
        plt.plot(x2, y2, label="cool")
        plt.plot(x3, y3, label="moderate")
        plt.plot(x4, y4, label="hot")
        plt.plot(x5, y5, label="very hot")
        plt.legend(loc='center right')


        plt.show()

    def getGraphCapacity(self):
        small = [-5,0,5]
        medium = [3,5,7]
        high = [5,10,15]
        x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
        for i in range(0,11):
            functionTriangleGraph(i, small, x1, y1)
            functionTriangleGraph(i, medium, x2, y2)
            functionTriangleGraph(i, high, x3, y3)
        plt.plot(x1, y1, label="small")
        plt.plot(x2, y2, label="medium")
        plt.plot(x3, y3, label="high")
        plt.show()

    def getGraphPower(self):
        small = [-10, 0, 10]
        medium = [5, 10, 15]
        high = [10, 20, 30]
        x1, y1, x2, y2, x3, y3 = [], [], [], [], [], []
        for i in range(0,21):
            functionTriangleGraph(i, small, x1, y1)
            functionTriangleGraph(i, medium, x2, y2)
            functionTriangleGraph(i, high, x3, y3)
        plt.plot(x1, y1, label="small")
        plt.plot(x2, y2, label="medium")
        plt.plot(x3, y3, label="high")
        plt.legend(loc='center right')
        plt.show()

    def getGraphTemperature(self):
        cold = [0, 15, 30, 50]
        cool = [30, 50, 70]
        moderate = [60, 70, 80]
        hot = [70, 90, 110]
        veryhot = [90, 110, 130, 150]
        x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = [], [], [], [], [], [], [], [], [], []
        for i in range(20, 121):
            functionTrapezGraph(i, cold, x1, y1)
            functionTriangleGraph(i, cool, x2, y2)
            functionTriangleGraph(i, moderate, x3, y3)
            functionTriangleGraph(i, hot, x4, y4)
            functionTrapezGraph(i, veryhot, x5, y5)
        plt.plot(x1, y1, label="cold")
        plt.plot(x2, y2, label="cool")
        plt.plot(x3, y3, label="moderate")
        plt.plot(x4, y4, label="hot")
        plt.plot(x5, y5, label="very hot")
        plt.show()

