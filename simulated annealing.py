# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:42:00 2024

@author: ACER
"""

import pandas as pd
import random
import math

def readDistances():
    """
    This method reads the example data and splits
    the data randomly into two sets to create a
    training and test data set.
    """
    
    # Read the example Data from the file.
    return pd.read_csv('distances.csv', sep=',', header=0)
    
distanceTable = readDistances()

def getDistance(cityA, cityB):
    return distanceTable.loc[cityA-1][cityB]

#########################################################
#########################################################
########### NO NOT CHANGE THE FORMER CODE! ##############
#########################################################
#########################################################

# Function to calculate total distance of a path
def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += getDistance(path[i], path[i+1])
    
    return total_distance

# Example: The distance between Berlin (1) and Hamburg (2)
print(f"The distance between Berlin and Hamburg is {getDistance(1, 2)}km.")


initial_journey = list(range(1, 80))
random.shuffle(initial_journey)
distance = calculate_total_distance(initial_journey)
print("Initial journey:", initial_journey)
print("distance:", distance)

bestDistance = distance
bestRoute = initial_journey.copy()

# Simulated annealing parameters
initial_temperature = 10000
cooling_rate = 0.995
temperature = initial_temperature
min_temperature = 1

iterations = 0

while temperature > min_temperature:
    improved = False
    for j in range(len(initial_journey) - 1):
        newJourney = bestRoute.copy()
        city1, city2 = random.sample(range(len(initial_journey)), 2)
        newJourney[city1], newJourney[city2] = newJourney[city2], newJourney[city1]
        distance = calculate_total_distance(newJourney)

        if distance < bestDistance:
            bestDistance = distance
            bestRoute = newJourney.copy()
            improved = True
        else:
            delta = distance - bestDistance
            acceptance_probability = math.exp(-delta / temperature)
            if random.random() < acceptance_probability:
                bestDistance = distance
                bestRoute = newJourney.copy()
                improved = True

    if not improved:
        break  

    temperature *= cooling_rate
    iterations += 1

print("The best route is", bestRoute)
print("The corresponding distance is", bestDistance)
print("Number of iterations:", iterations)
