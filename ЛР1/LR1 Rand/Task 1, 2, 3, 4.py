import numpy as np
import collections
import matplotlib.pyplot as plt

filename = input("Enter name of .txt file: ")
data = np.genfromtxt(filename, dtype='float')


count = collections.Counter(data)
count = sorted(count.items())
max_count = 0
f = open("result.txt", "w+")
f.write("\n Name & Views | Count | Total count")
f.write("\n -------------+-------+------------")
print("Name & Views| Count | Total Count ")
print("------------+-------+-------------")
for i in range(len(count)):
    if (max_count < count[i][0]*count[i][1]):
        max_count = count[i][0]*count[i][1]
    f.write("\n\t " + str(count[i][0]) + " \t|   " + str(count[i][1]) + "   |\t" + str(count[i][0] * count[i][1]))
    if int(count[i][0]) < 10:
        print("\t" + str(count[i][0]) + "\t\t|   " + str(count[i][1])+"   |\t" + str(count[i][0]*count[i][1]))
    else:
        print("\t" + str(count[i][0]) + "\t|   " + str(count[i][1])+"   |\t" + str(count[i][0]*count[i][1]))
f.write("\n")


freq = [i[1] for i in count]
months_num = [i[0] for i in count]
totalCount = [0 for i in range(len(count))]


print("\nMax count of views = " + str(max_count))
for i in range(len(count)):
    totalCount[i] = count[i][0] * count[i][1]
for i in range(int(len(freq))):
    if (freq[i] == max(freq)):
       maxnumber = ('Number = ' + str(months_num[i]) + ' Freq = ' + str(freq[i]))
    if (totalCount[i] == max(totalCount)):
        maxfilm = ('Film = ' + str(months_num[i]) + ' Views = ' + str(totalCount[i]))
modaen = 'moda of entry data: ' + maxnumber
modaf = 'moda of film: ' + maxfilm
print(modaen)
print(modaf)


data = sorted(data)
medianaen = 'mediana of entry data = ' + str(data[int(len(data)/2)])
print(medianaen)

sumX = 0
for i in range(int(len(freq))):
    sumX += int(months_num[i]) * freq[i]
sumX = sumX/int(len(data))
averagesum = "Середнє значення: "+str(round(sumX, 3))
print(averagesum)

varX = 0
for i in range(int(len(data))):
    varX += (int(data[i]) - sumX)**2
varX = varX/(int(len(data))-1)
disp = "Дисперсія: " + str(round(varX, 3))
print(disp)
varX = np.sqrt(varX)
averagequad = "Середнє квадратичне відхилення: " + str(round(varX, 3))
print(averagequad)



f.write(modaen + "\n" + modaf + "\n" + medianaen + "\n" + averagesum + "\n" + disp + "\n" + averagequad)
f.close()


months_numstr = ["" for i in range(len(months_num))]
for i in range(len(months_num)):
    months_numstr[i] = str(months_num[i])
f, ax = plt.subplots()
x = months_numstr
plt.bar(x, totalCount, 0.8, color='g', align='center')
ax.set_xticks(x)
ax.set_yticks(totalCount)
plt.ylabel("Views")
plt.xlabel("Names of Films")
plt.title("Table Films")
plt.show()
