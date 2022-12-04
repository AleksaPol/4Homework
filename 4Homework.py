# 1. Вычислить число c заданной точностью d # Пример: - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import sympy
import random
print('Задача 1.')
d = float(input(
    'Введите точность d (10^{-1} ≤ d ≤10^{-10}) для вычисления числа Пи: '))
d = str(d)
fif = d.find('.')
c = d[fif+1::]
a = 1
x = 0
for a in range(1, 1000000):
    x = x+4*((-1)**(a+1))/(2*a-1)
print(round(x, len(c)))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
print('_________________________________________________________________________________________')
print('Задача 2.')
a = 5
b = a % 1
num = int(input("Введите число: "))
i = 2
lst = []
while i <= num:
    if num % i == 0:
        lst.append(i)
        num = num / i
        i = 2
    else:
        i += 1
print(f"Простые множители числа приведены в списке: {lst}")

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
print('_________________________________________________________________________________________')
print('Задача 3.')
lst = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Исходная последовательность: {lst}')
newList = []
for i in lst:
    if lst.count(i) == 1:
        newList.append(i)
print(f'Cписок неповторяющихся элементов: {newList}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. # Пример: #  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
print('_________________________________________________________________________________________')
print('Задача 4.')


def create_pol(n):
    polinom = ''
    for i in range(n+1):
        if i == 0:
            polinom += str(random.randint(1, 100)) + '*x^' + str(n - i)
        elif i == n:
            polinom += '+' + str(random.randint(1, 100))
        else:
            polinom += '+' + str(random.randint(1, 100)) + '*x^' + str(n - i)
    polinom += ' = 0'
    return polinom


n = int(input('Задайте натуральную степень k: '))
with open('createpol.txt', 'w') as data:
    data.write(create_pol(n))
with open('createpol.txt', 'r') as data1:
    cp = data1.read()
print(cp)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
print('_________________________________________________________________________________________')
print('Задача 5.')
x = sympy.Symbol('x')
with open('pol1.txt', 'r') as data1:
    p1 = data1.read()
print(p1)
with open('pol2.txt', 'r') as data2:
    p2 = data2.read()
print(p2)
c = sympy.simplify(p1+'+'+p2)
with open('res.txt', 'w') as data3:
    data3.write(str(c))
print(c)
