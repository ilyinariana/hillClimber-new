# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 14:59:48 2023

@author: ThomasKopsch
"""

import pandas as pd


# The task is to implement the hillClimber algorithm.
# Find a 'good' solution to the Travelling salesman
# problem using the hillClimber algorithm.
#
# The distances of 80 large German cities is provided.
# Each city is encoded with a number 1-80.
# You can find a legend in the accompanieng documents.


#########################################################
#########################################################
######### NO NOT CHANGE THE FOLLOWING CODE! #############
#########################################################
#########################################################

def readDistances():
    """
    This method reads the example data and splits
    the data randomly into two sets to create a
    training and test data set.
    """
    
    # Read the example Data from the file.
    return pd.read_csv('distances.csv', sep=',', header=0)

def readCities():
    return pd.read_excel('legend.xlsx')

#Global variables to store the distance table and cities

    
distanceTable = readDistances()
citiesData = readCities()

def getDistance(cityA, cityB):
    return distanceTable.loc[cityA-1][cityB]



#########################################################
#########################################################
########### NO NOT CHANGE THE FORMER CODE! ##############
#########################################################
#########################################################

#Function to get city name by city number

def getCityName(cityNumber):
    return citiesData.loc[cityNumber - 1]['City Name']

#Implementation of hillClimber algorithm

def hillClimber(start_city):
    current_city = start_city
    unvisited_cities = set(range(1, 81)) - {start_city}
    path = [start_city]
    
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: getDistance(current_city, city))
        path.append(next_city)
        unvisited_cities.remove(next_city)
        current_city = next_city
    path.append(start_city) #return to the starting city to complete the loop
    return path

# Function to calculate total distance of a path
def calculate_total_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += getDistance(path[i], path[i+1])
    return total_distance

#Call the hillClimber function to get the solution path
solution_path = hillClimber(1)
# Calculate total distance of the solution path
total_distance_traveled = calculate_total_distance(solution_path)

# Print the total distance traveled
print("Total distance traveled:", total_distance_traveled, "km")


# Example: The distance between Berlin (1) and Hamburg (2)
print(f"The distance between Berlin and Hamburg is {getDistance(1,2)}km.")

city_names = [getCityName(city) for city in solution_path]
print("Solution path:", city_names)



