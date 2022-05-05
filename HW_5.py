import string


def  my_Compare_function (a,b):
    if (a > b):
        return (f' {a} is greater than {b} + "Both of numbers positive"')
    else:
        return (f' {a} is less than {b} + "Both of numbers positive"')



def  my_Compare_positive(a,b):
    if (a >0) and  (b>0):

        return ("Both of numbers positive")

    else:
        return ( "Can compare only positive numbers!")



def  my_Compare_sum (a,b):
    print(f'RESULTAT {a+b} ')


def  my_Compare_sub (a,b):
    print(f'RESULTAT {a - b} ')


def taske(a):
    b="<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    c=">>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    d="Task # "

    print(b,d,a,c)


def casee(n):
    b = "~~~~~~~~~~~~~~~"
    c = "~~~~~~~~~~~~~~~"
    d = "case # "

    print(b, d, n, c)

#
# taske(5)
# casee(1)
#  # 1) Write a function to compare 2 numbers.
# 	# E.g. compare(2, 3) should return False otherwise should return True.
# a = 2
# b =3
# my_Compare_function(a,b)
# print(my_Compare_function(a,b))
#
# taske(5)
# casee(2)
#
# user_input = int(input("Введите числа: "))
# user_input2= int(input("Введите числа: "))
# result = my_Compare_positive(user_input,user_input2)
# print(result)

# taske(5)
# casee(3)
# user_input = int(input("Введите числа: "))
# user_input2= int(input("Введите числа: "))
#
# my_Compare_sum(user_input,user_input2)

# taske(5)
# casee(4)
# user_input = int(input("Введите числа: "))
# user_input2= int(input("Введите числа: "))
#
# my_Compare_sub(user_input,user_input2)

# taske(5)
# casee(5)
# def returns_type(t: str) -> str:
#     if isinstance(t,str):
#         return f'It is string " {(type(t))}.'
#     else:
#         return "It is not string"
#
# user_input = input('Please, enter your favorite string: ')
# result = returns_type(user_input)
# print(result)
#
# print('Banana', end=' ')
# print('pudding.')
# taske(5)
# casee(6)
# def print_vertical(t : str) ->str:
#     for letter in t:
#        print(letter)
#
# user_input = input('Please, enter your favorite string: ')
# result = print_vertical(user_input)
def contac (abc, dred :str ):
    return  abc+dred


user_input = input("Enter your first phase: " )
user_input2 = input("Enter your second phase: ")
result = contac(user_input,user_input2)
print(result)



