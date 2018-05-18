#i/usr/bin/python
import pandas as pd

class Graph:
    
    def getTripsForTesting(dataFile):
        linkList = dataFile.linkId
        dateList = dataFile.DataAsOf
        speedList = dataFile.Speed
        travelTimeList = dataFile.TravelTime
        index = 0
        counter = 0
        
        testLinkSet = []
        testSpeedList = []
        testActualTimeSet = []
        testRequestedTimeSet = []
        
        for day in range(1, 2):            
            testDate = dateList[index]
            
            while(testDate[2] == str(day)):
                tripLinkList = []
                tripSpeedList = []
                tripTravelTime = []
            
                while( len(tripLinkList) < 20 ):
                    if(len(str(day)) == 1):
                        if(testDate[2] == str(day)):
                            tripRequestedTime = str(testDate[9]) + str(testDate[10])
                            tripLinkList.append(linkList.get(index))
                            tripSpeedList.append(speedList.get(index))
                            tripTravelTime.append(travelTimeList.get(index))
                    elif(len(str(day)) == 2):
                        if(testDate[3] == str(day[1])):
                            tripRequestedTime = str(testDate[10]) + str(testDate[11])
                            tripLinkList.append(linkList.get(index))
                            tripSpeedList.append(speedList.get(index))  
                            tripTravelTime.append(travelTimeList.get(index))
                    index += 1
                counter += 1
#                print("Trip set ", str(counter), " : ", tripLinkList)
#                print("Speed set : ", tripSpeedList)
#                print("\n")
                
                actualTime = (sum(tripTravelTime))/60
                
                testLinkSet.append(tripLinkList)
                testSpeedList.append(tripSpeedList)
                testActualTimeSet.append(actualTime)
                testRequestedTimeSet.append(tripRequestedTime)
                if(len(testLinkSet) == 10):
                    break                
            testDate = dateList[index]
            print("Link List : ", testLinkSet)
            print("Speed List : ", testSpeedList)
            print("Actual Time List : ", testActualTimeSet)
            print("Requested Time List : ", testRequestedTimeSet)
        return testLinkSet, testSpeedList, testRequestedTimeSet, testActualTimeSet;
            

                

                        
