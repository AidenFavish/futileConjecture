def oddEven(num):
    stick1 = num/2
    if int(stick1)*2 == num:
        return "even"
    else:
        return "odd"
base2 = []
for i in range(0, 25):
    base2.append(2**i)
for i in range(1, 1001):
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
        if holder1 > peak:
            peak = holder1
            peakSteps = counter1
    if (2**counter1 != i):
        print(str(i) + " : " + str(counter1) + " : ( " + str(baseHit) + " in " + str(baseSteps) + " counts ) : [ " + str(peak) + " in " + str(peakSteps) + " counts ]")
print("ignoring all 2^x integers")