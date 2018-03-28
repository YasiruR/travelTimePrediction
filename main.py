#i/usr/bin/python
from speed_array import Day
from refine import BoxPlotTechnique
from average_time import AverageTime
from delta_function import Delta
import pandas as pd

class Main:
        
    def getDeltaArray(linkArray, lengthList, timeRequested):
        deltaValueList = []
        dayList = []
        updatedTravelTimeList = []
        currentSpeedList = [30, 18, 42]
        totalLength = sum(lengthList)
        dataFile = pd.read_csv('september2016.csv')
        #dataFile = pd.read_csv('august2016.csv')
        
        for day in range(1, 31): #September only
            print("\n Day ", str(day), " : ")
            linkList, speedList, travelTimeList, tripIdList = Day.getSpeedArray(day, timeRequested, linkArray, dataFile)
            print("Trip ID list : ", tripIdList)
            print("Link list : ", linkList)
            print("Speed list : ", speedList)
            print("Travel Time list : ", travelTimeList)
            deltaValue = Delta.deltaFunction(linkList, lengthList, speedList, currentSpeedList, totalLength) 
            print("Delta Value : ", deltaValue)
            if(len(linkArray) == len(linkList)):
                dayList.append(day)
                updatedTravelTimeList.append(travelTimeList)
                deltaValueList.append(deltaValue)
            else:
                print("NOT ADDED TO THE LIST")
                pass
        refinedDayList, refinedDeltaValueList, refinedTravelTimeList = BoxPlotTechnique.refineDeltaArray(dayList, deltaValueList, updatedTravelTimeList)
        print("\nRefined Day List : ", refinedDayList)
        print("\nRefined Travel Time List : ", refinedTravelTimeList)
        print("\nRefined Delta Value List : ", refinedDeltaValueList)
        averageTime = AverageTime.calculateAverageTime(refinedDayList, refinedTravelTimeList)
        print("\n \n")
        print("Calculated average time to travel : ", (averageTime/60), " min")
        
        return;

linkArray = [4616266, 4362342, 4362244]
timeRequested = 18
lengthArray = []

for i in range(len(linkArray)):
    lengthArray.append(10)
    
Main.getDeltaArray(linkArray, lengthArray, timeRequested)