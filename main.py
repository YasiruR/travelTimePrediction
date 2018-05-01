#i/usr/bin/python
from speed_array import Day
from refine import BoxPlotTechnique
from average_time import AverageTime
from delta_function import Delta
import pandas as pd
import sys

class Main:
        
    def getDeltaArray(linkArray, lengthList, timeRequested, currentSpeedList):
        deltaValueList = []
        dayList = []
        updatedTravelTimeList = []
        totalLength = sum(lengthList)
        #dataFile = pd.read_csv('september2016.csv')
        dataFile = pd.read_csv('august2016.csv')
        
        for day in range(1, 31): #September only
            print("\n Day ", str(day), " : ")
            linkList, speedList, travelTimeList, tripIdList = Day.getSpeedArray(day, timeRequested, linkArray, dataFile)
            print("Trip ID list : ", tripIdList)
            #print("Link list : ", linkList)
            #print("Speed list : ", speedList)
            #print("Travel Time list : ", travelTimeList)
            deltaValue = Delta.deltaFunction(linkList, lengthList, speedList, currentSpeedList, totalLength) 
            print("Delta Value : ", deltaValue)
            if(len(linkArray) == len(linkList)):
                dayList.append(day)
                updatedTravelTimeList.append(travelTimeList)
                deltaValueList.append(deltaValue)
                timeLoss = str(abs(actualTime1 - sum(travelTimeList)) / 60)
                sys.stdout.write('\rTime deviation : ' + timeLoss + '\n')
            else:
                print("NOT ADDED TO THE LIST")
                pass
        refinedDayList, refinedDeltaValueList, refinedTravelTimeList = BoxPlotTechnique.refineDeltaArray(dayList, deltaValueList, updatedTravelTimeList)
        print("\nRefined Day List : ", refinedDayList)
        print("\nRefined Travel Time List : ", refinedTravelTimeList)
        print("\nRefined Delta Value List : ", refinedDeltaValueList)
        averageTime = AverageTime.calculateAverageTime(refinedDayList, refinedTravelTimeList)
        print("\n \n")
        print("Calculated average time to travel : ", (averageTime/60), "min")
        
        return averageTime;

#linkArray = [4616266, 4362342, 4362244]
#currentSpeedList = [30, 18, 42]
        
currentSpeedList1 = [62.76, 60.89, 55.92, 65.87, 60.89, 65.87]
linkArray1 = [4616213, 4616214, 4616215, 4616212, 4616198, 4616202]
actualTime1 = (125+82+133+49+100+79)/60
timeRequested1 = '11'

#currentSpeedList2 = [41.01, 39.15, 49.09, 45.98, 47.22, 44.12]
#linkArray2 = [4456481, 4456452, 4456505, 4456506, 4763656, 4616218]
#actualTime2 = (180+62+140+149+84+49) / 60
#timeRequested2 = '03'

#currentSpeedList3 = [59.03, 45.98, 3.73, 34.8]
#linkArray3 = [4616250, 4456498, 4362342, 4616365]
#actualTime3 = (69+54+57+437) / 60
#timeRequested3 = '02'

lengthArray = []

for i in range(len(linkArray1)):
    lengthArray.append(10)
    
averageTime = Main.getDeltaArray(linkArray1, lengthArray, timeRequested1, currentSpeedList1)

print("\nActual time : ", actualTime1, "min")
percentDeviation = ((abs((averageTime/60) - actualTime1)) / actualTime1) * 100
print("\nDeviation error percentage : ", percentDeviation, "%")