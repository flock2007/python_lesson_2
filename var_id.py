temp_var_1 = input('введите что-нибудь: ')
print(temp_var_1, type(temp_var_1),id(temp_var_1))

temp_var_2 = input('введите что-нибудь снова: ')
print(temp_var_2, type(temp_var_2),id(temp_var_2))

temp_var_1 = temp_var_2
temp_var_1 = int(temp_var_2)
print(temp_var_1, type(temp_var_1),id(temp_var_1))

temp_float = input('введите любое число: ')
print(temp_float, type(temp_float),id(temp_float))

if temp_float.isdigit():
    temp_float=float(temp_float)
    print(temp_float, type(temp_float), id(temp_float))
else:
    print("Это не число!")