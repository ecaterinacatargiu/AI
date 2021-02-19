# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy
from scipy.stats import uniform



def binomialDistribution():
    plt.plot(numpy.random.binomial(101, 0.7, 100), 'ro')
    plt.axis([ -1, 101, 0, 101])
    plt.ylabel('Numbers')
    plt.show()
    
    
def uniformDistribution():
    plt.plot(numpy.random.uniform(50, 0.6, 100), 'ro')
    plt.axis([-1, 101, 0, 101])
    plt.ylabel("Numbers")
    plt.xlabel("Numbers")
    plt.show()
    
def exponentialDistribution():
    plt.plot(numpy.random.exponential(5, 100), 'ro')
    plt.axis([-1, 101, 0, 101])
    plt.ylabel("Numbers")
    plt.xlabel("Numbers")
    plt.show()
    
def geometricDistribution():
    plt.plot(numpy.random.geometric(0.35, 10000), 'ro')
    plt.axis([-1, 101, 0, 101])
    plt.ylabel("Numbers")
    plt.xlabel("Numbers")
    plt.show()
    
def poissonDistribution():
    plt.plot(numpy.random.poisson(5, 1000), 'ro')
    plt.axis([-1, 101, 0, 101])
    plt.ylabel("Numbers")
    plt.xlabel("Numbers")
    plt.show()
    
def negativeBinomialDistribution():
    plt.plot(numpy.random.negative_binomial(1, 0.1, 1000), 'ro')
    plt.axis([-1, 101, 0, 101])
    plt.ylabel("Numbers")
    plt.xlabel("Numbers")
    plt.show()
    
def hypergeometricDistribution():
    plt.plot(numpy.random.hypergeometric(15,15,15,10000), 'ro')
    plt.axis([-1, 101, 0, 101])
    plt.ylabel("Numbers")
    plt.xlabel("Numbers")
    plt.show()
    


def main():
    print("Welcome to distributions carnival!")
    while True :
        option = input("Please input your choice: ")
        if option== "1" :
            print("Binomial distribution")
            binomialDistribution()
        else:
            if option == "2" :
                print("Uniform distribution")
                uniformDistribution()
            else:
                if option == "3":
                    print("Exponential distribution")
                    exponentialDistribution()
                else:
                    if option == "4":
                        print("Geometric distribution")
                        geometricDistribution()
                    else:
                        if option == "5":
                            print("Poisson Distribution")
                            poissonDistribution()
                        else:
                            if option == "6":
                                print("Negative-binomial Distribution")
                                negativeBinomialDistribution()
                            else:
                                if option == "7":
                                    print("Hypergeometric Distribution")
                                    hypergeometricDistribution()
                                else:
                                    if option == "0":
                                        break
                                    else:
                                        print("Invalid option!")
                            

        


main()


