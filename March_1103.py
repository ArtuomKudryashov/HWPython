# Используя стандартные
# Какие из представленных выражений можно преобразовать в целое десятичное число за одну операцию:
# А) '123е';
# Б) '91.4';
# В) 524.345 ** 435345345311145345;
# Г) '7.1 + 4';
# Д) '4' - 2;
# Е) '4 - 2';
# Ж) '42'
# З) -12.12?
# From Me to Everyone 08:17 PM



print (4 ** 4 ** 4)
print (4 * 4 * 4)

print  ( int ("123"))
# print (int("4-2"))
print (type('42'))
print (524.345 **2 )
a =10.8
print (int (a))

x = 5
y = 8
print((float()))

a = 5
print(a == int (5))

x = [1, 2, 3,4,5]
# Дан произвольный список.
# Представьте его в обратном порядке.

print(x)
print (x[::-1])
print (x)
x.reverse()
print(x)
	# Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.

x = [1, 2, 3,4,5]
def  change (list):
    temp = list.pop()
    list.insert (0, temp)
    temp = list.pop(1)
    list.append(temp)
    return  list
print(change(x))

temp = x.pop()
print(x)
print(temp)
# 2 швг



