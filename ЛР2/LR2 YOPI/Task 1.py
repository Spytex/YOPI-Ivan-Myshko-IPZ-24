import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
data = [0]
f = open("result.txt", "w+")


def connectTxT(data):
    NameOfFile = input("Input txt file: ")
    data = np.genfromtxt(NameOfFile, dtype='int')
    data = np.delete(data,0)
    print("Unsorted data: ", data)
    f.write("Unsorted data: " + str(data))
    data = sorted(data)
    print("\nSorted data: ", data)
    f.write("\nSorted data: " + str(data) + "\n\n")
    return data


def getFirstDigit(num):
    gg = ""
    for i in range(len(str(num))-1):
        gg += str(num)[i]
    return gg


def Pfunc(x, SortedData):
    index = x * (len(SortedData) + 1) - 1
    Percentile = SortedData[int(index)] + (index % int(index)) * (SortedData[int(index) + 1] - SortedData[int(index)])
    return Percentile


def StandartDeviation(data):
    sum = 0
    totalSum = 0
    for i in range(len(data)):
        sum += data[i]
    midleX = sum / len(data)

    for i in range(len(data)):
        totalSum += (data[i] - midleX)**2
    return np.sqrt(totalSum/(len(data)-1))

def AverageDeviation(data):
    sum = 0
    totalSum = 0
    for i in range(len(data)):
        sum += data[i]
    midleX = sum / len(data)
    for i in range(len(data)):
        totalSum += abs(data[i] - midleX)
    return totalSum/(len(data))


def boxdiagram(data):
    plt.figure(figsize=(10, 7))
    # Creating plot
    plt.boxplot(data)
    plt.grid()
    # show plot
    plt.show()


def lineal(data):
    sum = 0
    result = []
    for i in range(len(data)):
        sum += data[i]
    midleX = sum / len(data)
    a = np.array([
        [100*1, 1, ],
        [1*midleX, 1, ]
    ])
    b = np.array([100, 95])
    x = solve(a, b)
    print("a = " + str(x[0]) + "\nb = " + str(x[1]))
    f.write("a = " + str(x[0]) + "\nb = " + str(x[1]))
    for i in range(len(data)):
        result.append(x[0]*data[i]+x[1])
    print("Result marks: " + str(result) + "\n\n")
    f.write("\nResult marks: " + str(result) + "\n\n")


data = connectTxT(data)
minimal = min(data)
maximal = max(data)
Q1 = Pfunc(1/4, data)
Q3 = Pfunc(3 / 4, data)
P90 = Pfunc(0.9, data)
print("\n\nLower(first) quartile = " + str(Q1))
f.write("Lower(first) quartile = " + str(Q1))
print("Upper(third) quartile = " + str(Q3))
f.write("\nUpper(third) quartile = " + str(Q3))
print("\n90-th percentile = " + str(P90))
f.write("\n\n90-th percentile = " + str(P90))
print("\nStandart Deviation = " + str(StandartDeviation(data)))
f.write("\n\nStandart Deviation = " + str(StandartDeviation(data)))
print("Average Deviation = " + str(AverageDeviation(data)) + "\n")
f.write("\nAverage Deviation = " + str(AverageDeviation(data)) + "\n\n")
lineal(data)

print("Stem-Leaf Diagram")
f.write("\nStem-Leaf Diagram")
def CreateTable(data):
    strnumbers = ""
    dd = []
    key = 0
    for i in range(len(data)):
        strnumbers += str(data[i]%10) + " "
        g = int(getFirstDigit(data[i]))
        j = i
        if (i == len(data)-1):
            dd.append(strnumbers)
            print(getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            f.write("\n" + getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            break
        elif (getFirstDigit(data[i]) != getFirstDigit(data[i+1])):
            dd.append(strnumbers)
            print(getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            f.write("\n" + getFirstDigit(data[i]) + " \t| \t" + strnumbers)
            strnumbers = ""
            g += 1
            while (g != int(getFirstDigit(data[i+1]))):
                print(str(g) + " \t| \t" + strnumbers)
                f.write("\n" + str(g) + " \t| \t" + strnumbers)
                g += 1
        while (j != len(data) and key == 0):
            if (int(getFirstDigit(data[i])) == int(getFirstDigit(data[j]))-1):
                key = data[i]
                break
            else:
                j += 1
    print("\nKey: " + str(key))
    f.write("\n\nKey: " + str(key))


CreateTable(data)
boxdiagram(data)
