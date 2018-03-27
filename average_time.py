#i/usr/bin/python

class AverageTime:

    def calculateAverageTime(dayArray, travelTimeArray):
        sumOfTotalTime = 0
        for index in range(len(dayArray)):
            totalTime = sum(travelTimeArray[index])
            sumOfTotalTime += totalTime
        averageTime = sumOfTotalTime / len(dayArray)
        return averageTime;
