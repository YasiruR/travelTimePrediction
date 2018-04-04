import requests
import json

coArray = [[40.74047,-74.009251], [40.74137,-74.00893], [40.7431706,-74.008591]]

#for ele in coArray:
#    strEle = str(ele)
#    strEle.replace(" ", "")
#    coEle = strEle[1:-1]
#    print(coEle, "\n")
#    coordinatesString += str(coEle) + ';'
#print(coordinatesString)

def mapArrayIntoUrl(coArray):
    
    coordinatesString = ""
    for ele in coArray:
        for gEle in ele:
            if(gEle == ele[0]):
                strEle = str(gEle) + ","
            else:
                strEle = str(gEle)
            coordinatesString += strEle
        if(ele != coArray[(len(coArray)-1)]):
            coordinatesString += ";"
    print(coordinatesString)
    return coordinatesString;

def getDistanceOSRM(coArray): 
    
    coordinatesString = mapArrayIntoUrl(coArray)
    url = 'http://router.project-osrm.org/route/v1/driving/' + coordinatesString + '?overview=false'
    print(url)
    
    response = requests.get(url)
    print("\nDistance : ", response.text)
    return;
    
getDistanceOSRM(coArray)
