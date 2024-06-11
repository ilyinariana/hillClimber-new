# -*- coding: utf-8 -*-
"""
Created on Wed May 22 19:56:56 2024

@author: ACER
"""

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
    total_distance += getDistance(path[-1], path[0])
    return total_distance





# Example: The distance between Berlin (1) and Hamburg (2)
print(f"The distance between Berlin and Hamburg is {getDistance(1,2)}km.")

# Function to generate all possible arrangements by swapping cities

   
initial_journey = list(range(1,80))
distance = calculate_total_distance(initial_journey)
print( "Initial journey:", initial_journey)
print("distance:", distance)

bestDistance = distance
bestRoute = initial_journey.copy()  
  
for i in range(100): 
    for j in range( len(initial_journey)-1 ):
    
        newJourney = initial_journey.copy()
        newJourney[j+1], newJourney[j] = newJourney[j], newJourney[j+1]
        distance = calculate_total_distance(newJourney)
    
        if distance<bestDistance:
            bestDistance = distance
            bestRoute = newJourney.copy()
    

    
print("The best route is", bestRoute )
print("The corresponding distance is", bestDistance)

bestDistance_1 = bestDistance 
bestRoute = newJourney.copy()  



  
for i in range(98): 
    for j in range( len(newJourney)-1 ):
    
        newJourney_2 = newJourney.copy()
        newJourney_2[j+1], newJourney_2[j] = newJourney_2[j], newJourney_2[j+1]
        distance = calculate_total_distance(newJourney_2)
    
        if distance<bestDistance_1:
            bestDistance_1 = distance
            bestRoute = newJourney_2.copy()
            
print("The best route is", bestRoute )
print("The corresponding distance is", bestDistance_1)

bestDistance_2 = bestDistance_1
bestRoute_2 =  newJourney_2.copy()
  
for i in range(5): 
    for j in range( len(newJourney)-1 ): 
        newJourney_3 = newJourney_2.copy()
        newJourney_3[j+1], newJourney_3[j] = newJourney_3[j], newJourney_3[j+1]
        distance = calculate_total_distance(newJourney_3)
    
        if distance<bestDistance_2:
          bestDistance_2 = distance
          bestRoute_2 = newJourney_3.copy()
            
       
    
   
            ### Endet hier
    

    
print("The best route is", bestRoute )
print("The corresponding distance is", bestDistance_2)







   






# Example: The distance between Berlin (1) and Hamburg (2)

#city_names = [getCityName(city) for city in solution_path]
#print("Solution path:", city_names)