
from collections import Counter
import math
import xlrd
import matplotlib.pyplot as plt

e = ''
x = []
time0, time1, time2 = [], [], []
t = int(input("Введите временной промежуток:"))
f = xlrd.open_workbook(input("Введите название файла:"), "r")  # открытие файла; в каждой строке: ФИО, год рождения
s = f.sheet_by_index(0)         # открывается лист с данными по периоду. Номер листа совпадает с номером периода
for row in range(s.nrows):
    b = []
    for col in range(s.ncols):
        b.append(s.cell(row, col))
    for i in range(len(b)):
        if i == 0:
            e = str(b[i])
        else:
            e = e + str(b[i])
    time0.append(e)         # создание массива с преобразованными данными по периоду. Одна строка = элементу масива

s = f.sheet_by_index(1)  # проделывается то же самое с листом 1 периода, считается число совпадений
for row in range(s.nrows):  # создает массив
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
    if b01[word] > 1:               # m01 - помеченные из выявленых во втором периоде
        m01 += 1

s = f.sheet_by_index(2)  # проделывается то же самое с листом 2 периода, считается число совпадений
for row in range(s.nrows):  # создает массив
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

N = (len(time01)*(len(time1)-m01)*(m01+m012))/(m01*(m12+m012))      # Вычисление общей ЧИСЛЕННОСТИ
SPEED = (1/t)*(math.log(m01*len(time1)/len(time0)*(m02+m012)))     # скорость роста популяции
speed = (1/t)*(math.log((len(time1)-m01))*(m02+m012))/len(time0)*(m12+m012)    # скорость снижения численности популяции

x.append(round(N))  # округление значений до целого, x - список с данными по численности в разные года


def number(gamma, beta, a):     # функция, которая на основе данных численности и скоростей роста и убывания
    N = a * ((math.exp(gamma) - math.floor(math.exp(gamma))) + (math.exp(beta) - math.floor(math.exp(beta))))
    return N                # считает новую численность (N для каждого года мненяется, speed и SPEED константы)


l = 2                                           # вычисление численности для 2 лет
while l > 0:
    N = number(speed, SPEED, N)
    l = l - 1
    x.append(round(N))   # округление значений
print(x)

plt.bar([t, t+t, 3*t], [x[0], x[1], x[2]], color='silver')
plt.plot([t, t+t, 3*t], [x[0], x[1], x[2]], color='red')
plt.title('Прирост числа инфицированных')
plt.ylabel('Количество человек')
plt.xlabel('Временной период')
plt.show()

