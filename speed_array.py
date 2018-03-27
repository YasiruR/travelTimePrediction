#i/usr/bin/python
import pandas as pd

class Day:

    def getSpeedArray(date, time, linkArray):
        
        #dataFile = open('september2016.csv', "r")
        #reader = csv.reader(dataFile)
        dFile = pd.read_csv('september2016.csv')
        tripIdList = dFile.Id
        travelTimeList = dFile.TravelTime
        linkList = dFile.linkId
        dateList = dFile.DataAsOf
        speedList = dFile.Speed
        
        selectedIndexList = []
        selectedSpeedList = []
        selectedLinkList = []
        selectedTravelTimeList = []
        selectedTripIdList = []
        
        finalIndexList = []
        finalLinkList = []
        finalSpeedList = []
        finalTravelTimeList = []
        finalTripIdList = []
        
        
        index = 0
        if(len(str(date)) == 1):     
            for ele in dateList:
                if((ele[2] == str(date)) & (ele[3] == "/")):
                    if((ele[9] == str(time)[0]) & (ele[10] == str(time)[1])):
                        selectedIndexList.append(index)
                        selectedSpeedList.append(speedList.get(index))
                        selectedLinkList.append(linkList.get(index))
                        selectedTravelTimeList.append(travelTimeList.get(index))
                        selectedTripIdList.append(tripIdList.get(index))
                index += 1
        elif(len(str(date)) == 2):
            for ele in dateList:
                if((ele[2] == str(date)[0]) & (ele[3] == str(date)[1])):
                    if((ele[10] == str(time)[0]) & (ele[11] == str(time)[1])):
                        selectedIndexList.append(index)
                        selectedSpeedList.append(speedList.get(index))
                        selectedLinkList.append(linkList.get(index))
                        selectedTravelTimeList.append(travelTimeList.get(index))
                        selectedTripIdList.append(tripIdList.get(index))
                index += 1
                
        
        for link in linkArray:
            #print("selecting ", link, " link")
            index = 0
            for linkEle in selectedLinkList:
                #print("checking with link ", linkEle)
                if(link == linkEle):
                    finalIndexList.append(selectedIndexList[index])
                    finalSpeedList.append(selectedSpeedList[index])
                    finalLinkList.append(linkEle)
                    finalTravelTimeList.append(selectedTravelTimeList[index])
                    finalTripIdList.append(selectedTripIdList[index])
                    #print("Trip ID: ", selectedTripIdList[index])
                    #print("Speed: ", selectedSpeedList[index])
                    break
                #print(link, linkEle)
                index += 1
        
        #print("Final link list:", finalLinkList)
        #print("Final speed list", finalSpeedList)
        #print("Final travel time list:", finalTravelTimeList)
        return finalLinkList, finalSpeedList, finalTravelTimeList, finalTripIdList;
    
#classDay = Day()
#Day.getSpeedArray(10, 18, [4616266, 4362342, 4362244])
            
            
            
    
