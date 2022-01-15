import pandas as pd
import csv
import statistics
import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
    data = fileData[0]
# print(data)

def mean(data):
    n = len(data)
    total = 0

    for x in data:
        total += int(x)

    mean = total/n
    # print(mean)
    return mean

squaredList = []

for number in data:
    a = int(number) - mean(data)
    a = a**2
    squaredList.append(a)
#print(squaredList)

# calculating sum

sum = 0

for i in squaredList:
    sum += i
# print(sum)

# diving the sum by the total values
n = len(data)
result = sum/(n-1)
# print(result)

# final square root
stand_dev = math.sqrt(result)
print(stand_dev)