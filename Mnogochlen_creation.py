from random import randint
import itertools

x1 = ''
x2 = ''
# CREATION OF THE FIRST POL
n = int(input('Введите степень для 1го многочлена: '))

def create_mnogochlen(a):
    for k in range(n, -1, -1):
        a += f'{randint(0, 100)}*x**{k} + '
    a += '= 0'
    return a

def clear_mnogochlen(a):
    for i in a:
        if 'x**1' in a:
            a = a.replace('x**1', 'x')
        if '*x**0' in a:
            a = a.replace('*x**0', '')
        if '+ = 0' in a:
            a = a.replace(' + =', ' =')
    return a

x1 = create_mnogochlen(x1)
x1 = clear_mnogochlen(x1)
print(x1)

with open('mnogochlen1.txt', 'w') as data:
    data.write(x1)

# CREATION OF THE SECOND POL
n = int(input('Введите степень для 2го многочлена: '))
x2 = create_mnogochlen(x2)
x2 = clear_mnogochlen(x2)
print(x2)


with open('mnogochlen2.txt', 'w') as data:
    data.write(x2)



