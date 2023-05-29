# Тип данных - список (list)
#

# Инициализация (генераторы)
list_temp = [] # пустой список, квадратные скобки
print(type(list_temp))
list_temp = [1.2, 2 , 3, 123, 'кошка', [4, 5,5 , 66, 7, ]] # список может быть в списке

for el in list_temp:
    print(el, type(el))

# команда list
list_str=list("VolvO12345678")
print(list_str)
    # обращение к элементам списка, подспискам
for i in range(len(list_temp)):
    print(i,": ",list_temp[i])

for i in range(len(list_temp)):
    print(i,": ",list_temp[i:])

for i in range(len(list_temp)):
    print(i,": ",list_temp[:i])

# Функции со списками

'len - длинна списка'
print(len(list_str))
print(len(list_temp))

# Операции со списком
print(list_temp + list_str) # объединение списков в один
print(list_temp*2) # дублирование списка

# Методы

'append - добавление 1 элемента в список'
integer_list= []
for i in range(10) : #заполним список
    integer_list.append(i)
    print(integer_list)
integer_list.append(0)
print(integer_list)

'remove - удаление 1 элемента из списка, удаляет первый совпавший во вхождению элемент'
integer_list.remove(0) #круглые скобки
print(integer_list)

'del - удаляет элемент по порядковому номеру'
del integer_list[3] #квадратные скобки
print(integer_list)

'reverse - перестановка элементов списка в обратном порядке'
integer_list.reverse()
print(integer_list)

'sort - сортировка списка'
integer_list= [1,7,4, 8,8 ,64,32,45,4,5]
integer_list.sort()
print(integer_list)

'insert - добавить в список, сначала отмечаем после какой позиции, а потом сами данные в кол-ве 1 шт'
integer_list.insert(4 , 777)
print(integer_list)

                               # обработка списков (map, filter, reduce )
'map - какое-то действие применяется к каждому элементу списка'
integer_list= [1,7,4, 8,8 ,64,32,45,4,5]
# map(function, list) ----> map -----> list(map)
# new_integer_list = list(map(str, integer_list)) # перевели все знакт к строке(буквам)
new_integer_list = list(map(lambda x: x**2, integer_list)) #возвели в квадрат каждый символ
print(new_integer_list)

'filter - применяется условие, выводим только подходящие под условия данные'
integer_list= [1,7,4, 8,8 ,64,32,45,4,5]
# filter(function, list) ----> filter -----> list(filter)
new_integer_list = list(filter(lambda x: x<10, integer_list))
print(new_integer_list)

'reduce - применить единую формулу на все элементы'
from functools import reduce

integer_list = [1, 2, 3, 4]
print(integer_list)
sum = reduce(lambda x, y: x+y, integer_list)
multiply = reduce (lambda x, y: x*y, integer_list)
print(sum, multiply)