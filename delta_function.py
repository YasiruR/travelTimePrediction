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
    
            try:
                delta = (l / totalLength) * ((1/cs - 1/s) ** 2)
            except ZeroDivisionError:
                #print("cs : ", str(cs))
                #print("s : ", str(s))
                print("error!")
                return 0
            totalDelta += delta
        #print("Total delta : ", totalDelta)
        return totalDelta;
    







