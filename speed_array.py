#i/usr/bin/python

class Day:

    def getSpeedArray(date, time, linkArray, dataFile):
        
        #dataFile = open('september2016.csv', "r")
        #reader = csv.reader(dataFile)
        
        tripIdList = dataFile.Id
        travelTimeList = dataFile.TravelTime
        linkList = dataFile.linkId
        dateList = dataFile.DataAsOf
        speedList = dataFile.Speed
        
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
        
        print("Link list for day", str(date), " : ", finalLinkList)
        print("Speed list for day", str(date), " : ", finalSpeedList)
        print("Travel time list for day", str(date), " : ", finalTravelTimeList)
        return finalLinkList, finalSpeedList, finalTravelTimeList, finalTripIdList;
    

            
            
    
