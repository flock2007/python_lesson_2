#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
# for i in range (1,6):
#     print('строка(', i , '): 0')


'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
# m = 0
# quantity_5 = 0
# while m < 10:
#     try:
#         number = int(input('введите цифру (от 0 до 9): '))
#     except ValueError:
#         print('должна быть введена цифра!')
#     if number < 0 or number >= 9:
#         print('должно быть введено число от 0 до 9!')
#     else:
#         #print('проверку от 0 до 10 прошло!')
#         m = m + 1
#         if number == 5:
#             quantity_5 += 1
# print('Число 5 встречается', quantity_5,'раз(a)')

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# ymn = 1
# for i in range(1,11):
#     ymn = ymn * i
# print(ymn)
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
#ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ
# import random
# try:
#     a=int(input("введите любое число 1: ")) #вводим минимально возможное число для рандома
#     b=int(input("введите любое число 2 больше 1го: ")) #вводим максимально возможное число для рандома
#     raschlenenka = random.randint(a,b) #выбираем рандомное число
#     print(raschlenenka)
#     raschlenenka = abs(raschlenenka) #модуль на случай отридцательных чисел
#     raschlenenka = str(raschlenenka)
#     count = len(raschlenenka) #считаем длину строки
#     print('кол-во цифр: ', count)
#     i=0
#     for i in range(0,count+1):
#         c=raschlenenka[i:i+1] #чере индекс выбираем по одной цифре с самой первой
#         print(c)
# except ValueError:
#     print("Вводить можно только числа, и второе число долно быть больше первого.")

#ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
# import random
# try:
#     a = int(input("введите любое число 1: "))
#     b = int(input("введите любое число 2 больше 1го: "))
#     chislo = random.randint(a,b)
#     print(chislo)
#     while chislo >= 1:
#         sifra = chislo%10 #остаток от деления числа на 10
#         print(sifra)
#         chislo = chislo//10 #убираем у числа последнюю цифру для нового витка цикла
# except ValueError:
#     print("Вводить можно только числа, и второе число долно быть больше первого.")

'''
Задача 6
Найти сумму цифр числа.
'''
# import random
# try:
#     a = int(input("введите любое число 1: "))
#     b = int(input("введите любое число 2 больше 1го: "))
#     chislo = random.randint(a,b)
#     print(chislo)
#     sum=0
#     while chislo >= 1:
#             sifra = chislo%10
#             sum=sum+sifra
#             chislo = chislo//10
#     print("сумма цифр этого числа: ", sum)
# except ValueError:
#     print("Вводить можно только числа, и второе число долно быть больше первого.")


'''
Задача 7
Найти произведение цифр числа.
'''
# import random
# try:
#     a = int(input("введите любое число 1: "))
#     b = int(input("введите любое число 2 больше 1го: "))
#     chislo = random.randint(a,b)
#     print(chislo)
#     ymn=1
#     while chislo >= 1:
#             sifra = chislo%10
#             ymn=ymn*sifra
#             chislo = chislo//10
#     print("произведение цифр числа: ", ymn)
# except ValueError:
#     print("Вводить можно только числа, и второе число долно быть больше первого.")
'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number>0:
#     if integer_number%10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number//10
# else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
# import random
# try:
#     a = int(input("введите любое число 1: "))
#     b = int(input("введите любое число 2 больше 1го: "))
#     chislo = random.randint(a,b)
#     print(chislo)
#     maximum=0
#     while chislo >= 1:
#             sifra = chislo%10
#             list = [maximum, sifra]
#             maximum = max(list)
#             chislo = chislo//10
#     print("максимальная цифра в числе: ", maximum)
# except ValueError:
#     print("Вводить можно только числа, и второе число долно быть больше первого.")

'''
Задача 10
Найти количество цифр 5 в числе
'''
# try:
#     number = abs(int(input('введите число: '))) #переводим  число, берем модуль
#     number=str(number) #возвращаем в строку
#     dln = len(number) #ищем длину строки
#     i=0
#     quantity_5=0
#     for i in range(0,dln):
#         cifra = int(number[dln-i-1:dln-i]) # перебираем все цыфры с конца
#
#         if cifra == 5:
#             quantity_5 += 1
#     print('Всего цифр в числе :', dln)
#     print('Из них пятерок: ', quantity_5)
# except ValueError:
#     print('вводить можно только числа!')

'Задание Ultra pro: "Угадай число"'
Igra = None
while igra != 'Yes' or igra != 'Y' or igra != 'y' or igra != 'No' or igra != 'N' or igra != 'n':
    print("Введите просто Yes или No, или хотя бы Y или N")
    igra = input('Давайте сыграем в игру: Вы загадываете число, а я его отгадываю?  Yes/No: ')
if igra == 'No' or igra == 'N' or igra == 'n'


