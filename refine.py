#i/usr/bin/python
import numpy as np

class BoxPlotTechnique:

    def refineDeltaArray(dayArray, deltaArray, travelTimeArray):
        npDeltaArray = np.array(deltaArray)
        q1 = float(np.percentile(npDeltaArray, 25))
        q3 = float(np.percentile(npDeltaArray, 75))
        iq = q3 - q1
        upperBound = q3 + float(1.5 * iq)
        lowerBound = q1 - float(1.5 * iq)
    
        refinedDeltaArray = []
        refinedTravelTimeArray = []
        refinedDayArray = []
        
        for delta in deltaArray:
            if((lowerBound <= delta) & (delta <= upperBound)):
                i = deltaArray.index(delta)
                refinedDeltaArray.append(delta)
                refinedTravelTimeArray.append(travelTimeArray[i])
                refinedDayArray.append(dayArray[i])
        return refinedDayArray, refinedDeltaArray, refinedTravelTimeArray;
                                
