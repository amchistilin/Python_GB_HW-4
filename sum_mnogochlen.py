import re
import itertools
# Получение данных из файла
file1 = 'mnogochlen1.txt'
file2 = 'mnogochlen2.txt'
file_sum = 'sum_mnogochlen.txt'


def read_polynomial(file):
    with open(str(file), 'r') as data:
        polynomial = data.read()
    return polynomial

def sum_not_x(mng1, mng2):
    not_x = 0
    for i in range(len(mng1)):
        if 'x' not in mng1[i]:
            not_x += int(mng1[i])
    for j in range(len(mng2)):
        if 'x' not in mng2[j]:
            not_x += int(mng2[j])
    return not_x


def sum_one_x(arr1, arr2):
    one_x = 0
    for i in range(len(arr1)):
        if len(arr1[i]) == 4:
            one_x += int(arr1[i][0:2])
        if len(arr1[i]) == 3:
            one_x += int(arr1[i][0])
    for k in range(len(arr2)):
        if len(arr2[k]) == 4:
            one_x += int(arr2[k][0:2])
        if len(arr2[k]) == 3:
            one_x += int(arr2[k][0])
    return str(one_x) + '*x'

def clear_onex_and_nox(arr):
    new = []
    for i in range(len(arr)):
        if len(arr[i]) != 1 and len(arr[i]) != 2 and len(arr[i]) != 3 and len(arr[i]) != 4:
            new.append(arr[i])
    return new

def keys_creation(arr):
    keys = []
    for i in range(len(arr)):
        keys.append(arr[i][2:])
    return keys

def meanings_creation(arr):
    keys = []
    for i in range(len(arr)):
        keys.append(arr[i][0:2])
    return keys



res_pol = []
pol1 = read_polynomial(file1)
pol2 = read_polynomial(file2)
pol1 = pol1.replace(' = 0', '')
pol2 = pol2.replace(' = 0', '')
new_pol1 = pol1.split(' + ')
new_pol2 = pol2.split(' + ')


# добавить ___ = sum_not_x

#sum_not_x(new_pol1, new_pol2)

sum1 = sum_one_x(new_pol1, new_pol2)
sum2 = sum_not_x(new_pol1, new_pol2)

ok1 = clear_onex_and_nox(new_pol1)
ok2 = clear_onex_and_nox(new_pol2)

answer = ok1 + ok2
print(sum1)
print(sum2)
print(*answer, sep=' + ')








#
