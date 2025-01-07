
from collections import Counter
import math
import xlrd
import matplotlib.pyplot as plt

e = ''
x = []
time0, time1, time2 = [], [], []
t = int(input("Enter time period:"))
f = xlrd.open_workbook(input("Enter file name:"), "r")  # opening file; in each line: full name, year of birth
s = f.sheet_by_index(0)         # a sheet with data for the period opens. The sheet number matches the period number
for row in range(s.nrows):
    b = []
    for col in range(s.ncols):
        b.append(s.cell(row, col))
    for i in range(len(b)):
        if i == 0:
            e = str(b[i])
        else:
            e = e + str(b[i])
    time0.append(e)         # creating an array with converted data by period. One row = array element

s = f.sheet_by_index(1)  # the same is done with the sheet of period 1, the number of matches is counted
for row in range(s.nrows):  # creates an array
    g = []
    for col in range(s.ncols):
        g.append(s.cell(row, col))
    for i in range(len(g)):
        if i == 0:
            e = str(g[i])
        else:
            e = e + str(g[i])
    time1.append(e)

time01 = list(time0+time1)

b01 = Counter(time01)
m01 = 0
for word in b01:
    if b01[word] > 1:               # m01 - marked from those identified in the second period
        m01 += 1

s = f.sheet_by_index(2)  # the same is done with the sheet of period 2, the number of matches is counted
for row in range(s.nrows):  # creates an array
    p = []
    for col in range(s.ncols):
        p.append(s.cell(row, col))
    for i in range(len(p)):
        if i == 0:
            e = str(p[i])
        else:
            e = e + str(p[i])
    time2.append(e)
time12 = list(time1+time2)
b12 = Counter(time12)
m12 = 0
for word in b12:
    if b12[word] > 1:
        m12 += 1
time02 = list(time0+time2)
b02 = Counter(time02)
m02 = 0
for word in b02:
    if b02[word] > 1:
        m02 += 1

time012 = list(time0+time12)
b012 = Counter(time012)
m012 = 0
for word in b012:
    if b012[word] > 1:
        m012 += 1

N = (len(time01)*(len(time1)-m01)*(m01+m012))/(m01*(m12+m012))      # Calculating the total NUMBER
SPEED = (1/t)*(math.log(m01*len(time1)/len(time0)*(m02+m012)))     # population growth rate
speed = (1/t)*(math.log((len(time1)-m01))*(m02+m012))/len(time0)*(m12+m012)    # rate of population decline

x.append(round(N))  # rounding values ​​to integers, x is a list with data on the number of people in different years


def number(gamma, beta, a):     # a function that, based on data on the number and rates of growth and decline,
    N = a * ((math.exp(gamma) - math.floor(math.exp(gamma))) + (math.exp(beta) - math.floor(math.exp(beta))))
    return N                # calculates the new number (N is different for each year, speed and SPEED are constants)

l = 2                                           # Calculation of the number for 2 years
while l > 0:
    N = number(speed, SPEED, N)
    l = l - 1
    x.append(round(N))   # rounding of values
print(x)

plt.bar([t, t+t, 3*t], [x[0], x[1], x[2]], color='silver')
plt.plot([t, t+t, 3*t], [x[0], x[1], x[2]], color='red')
plt.title('Increase in the number of infected')
plt.ylabel('Number of people')
plt.xlabel('Time period')
plt.show()

