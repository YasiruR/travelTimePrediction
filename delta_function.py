#i/usr/bin/python
from speed_array import Day
from refine import BoxPlotTechnique

def getDeltaArray(linkArray, lengthList, timeRequested):
    #current speed values obtained (or else recent values) -> currentSpeedArray
    #for day in dayArray:
    #   values of v (speed) for the selected links on each day around time t are obtained
    #           -> speedArray
    #   delta = deltaFunction(...)
    #   deltaArray.append(delta)
    #return dayArray, deltaArray
    deltaValueList = []
    #idList = []
    dayList = []
    updatedTravelTimeList = []
    currentSpeedList = [30, 18, 42]
    totalLength = sum(lengthList)
    for day in range(1, 31): #September only
        print("\n Day ", str(day), " : ")
        linkList, speedList, travelTimeList, tripIdList = Day.getSpeedArray(day, timeRequested, linkArray)
        print("Trip ID list : ", tripIdList)
        print("Link list : ", linkList)
        print("Speed list : ", speedList)
        print("Travel Time list : ", travelTimeList)
        deltaValue = deltaFunction(linkList, lengthList, speedList, currentSpeedList, totalLength) 
        print("Delta Value : ", deltaValue)
        if(len(linkArray) == len(linkList)):
            dayList.append(day)
            updatedTravelTimeList.append(travelTimeList)
            deltaValueList.append(deltaValue)
        else:
            print("NOT ADDED TO THE LIST")
    refinedDayList, refinedDeltaValueList, refinedTravelTimeList = BoxPlotTechnique.refineDeltaArray(dayList, deltaValueList, updatedTravelTimeList)
    print("\nRefined Day List : ", refinedDayList)
    print("\nRefined Travel Time List : ", refinedTravelTimeList)
    print("\nRefined Delta Value List : ", refinedDeltaValueList)
    averageTime = calculateAverageTime(refinedDayList, refinedTravelTimeList)
    print("\n \n")
    print("Calculated average time to travel : ", (averageTime/60), " min")
    return;


def deltaFunction( linkArray, lengthArray, speedArray, currentSpeedArray, totalLength):
    totalDelta = 0
    delta = 0
    for i in range(len(linkArray)) :
        #link = linkArray[i]
        l = float(lengthArray[i])
        s = float(speedArray[i])
        cs = float(currentSpeedArray[i])

        delta = (l / totalLength) * ((1/cs - 1/s) ** 2)
        totalDelta += delta
    return totalDelta;

def calculateAverageTime(dayArray, travelTimeArray):
    sumOfTotalTime = 0
    for index in range(len(dayArray)):
        totalTime = sum(travelTimeArray[index])
        sumOfTotalTime += totalTime
    averageTime = sumOfTotalTime / len(dayArray)
    return averageTime;

linkArray = [4616266, 4362342, 4362244]
lengthArray = [10, 10, 10]
timeRequested = 18
getDeltaArray(linkArray, lengthArray, timeRequested)

#print('Total Length: ', totalLength)
#print(deltaFunction(linkArray, lengthArray, speedArray, currentSpeedArray, totalLength))







