#Простейший while
#
# i=0
# while i < 10:
#     print(i)
#     i = i+1
#     if i==5:
#       break
#
# answer= None
# while answer != 'kia' and answer != 'Kia':
#     answer = input('какая марка машин самая лучшая?: ')
#     if answer != 'kia' and answer != 'Kia':
#         print("Подумайте еще...")
# print("Вы абсолютно правы!")
#
# while i < 10:
#     print(i)
#     i = i+1
#     if i == 9:
#       break
#     if i < 3:
#       continue

for i in range(0, 10, 1): #range(start, stop (i-1), step)
    print (i)
    if i == 5 :
        break

for i in range(10):
    answer = input('какая марка машин лучше всего? ')
    if answer == 'kia' or 'Kia':
        print("я полностью согласен!")
        break

for i in range(0, 10, 1):  # range(start, stop (i-1), step)
    if i == 9:
       break
    if i <3 :
       continue
    else:
        print(i)
