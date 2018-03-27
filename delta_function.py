#i/usr/bin/python

class Delta:

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
    







