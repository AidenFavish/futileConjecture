def oddEven(num):
    stick1 = num/2
    if int(stick1)*2 == num:
        return "even"
    else:
        return "odd"
base2 = []
commonBaseDict = {}
commonPeakDict = {}
for i in range(0, 46):
    base2.append(2**i)
top = [0, 0]
slopeC = 0
slopeS = 0
slopeArray = []
for i in range(1, 10001):
    counter1 = 0
    holder1 = i
    base = False
    baseHit = 0
    baseSteps = 0
    peak = 0
    peakSteps = 0
    while holder1 != 1:
        if oddEven(holder1) == "odd":
            holder1 = (holder1*3)+1
        else:
            holder1 = holder1/2
        counter1 += 1
        if (holder1 in base2) and (base == False):
            baseHit = holder1
            base = True
            baseSteps = counter1
            if baseHit == 16:
                slopeS += 1
        if holder1 > peak:
            peak = holder1
            peakSteps = counter1
    if top[0] < peak:
        top = [peak, i]
    if (2**counter1 != i):
        print(str(i) + " : " + str(counter1) + " : ( " + str(baseHit) + " in " + str(baseSteps) + " counts ) : [ " + str(peak) + " in " + str(peakSteps) + " counts ]")
        if str(int(peak)) in commonPeakDict:
            commonPeakDict[str(int(peak))] += 1
        else:
            commonPeakDict[str(int(peak))] = 1
        if str(int(baseHit)) in commonBaseDict:
            commonBaseDict[str(int(baseHit))] += 1
        else:
            commonBaseDict[str(int(baseHit))] = 1
        if slopeC >= 1000:
            slopeC = 0
            slopeArray.append(slopeS/1000)
            slopeS = 0
        else:
            slopeC += 1
print("ignoring all 2^x integers")
print(commonBaseDict)
#print(commonPeakDict)
print(top)
slopeSum = 0
for i in slopeArray:
    slopeSum += i
print(slopeArray)
print(slopeSum/len(slopeArray))