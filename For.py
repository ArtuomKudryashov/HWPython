x = "Word"
for letter in x:
    print(letter)

lst = ["hi ", "Artuom", "How", "are", "you"]
for  element  in  lst :
    if  element == "are":

            continue

            print(element)



a= 10
b =10

if  a< 11:

    print ("a is less than b")
elif a==b:
    print ("Ok")

a = int(input("Enter a number"))
b = int (input("Enter one more number"))
operation = input("Enter operation")
if operation == "*":
    print(a*b)
elif operation == "/":
    if b ==0:
         print("Что-то не так")
    else:
          print(a/b)
elif operation == "+":
    print(a + b)
elif operation == "-":
    print(a-b)
else:
    print("Invalid operation")
    number1 = input("Enter the first number ")
    number2 = input("Enter the second number ")
    operation = input("Enter * for multiple, / for division, + for sum, - for subtraction: ")
    while not number1.isdigit():
        print("Give me a number!!!")
        number1 = input("Enter the first number ")
    while not number2.isdigit():
        print("Give me a number!!!")
        number2 = input("Enter the second number ")
    while operation not in ['*', '/', '+', '-']:
        print("Enter the correct operand ")
        operation = input("Enter * for multiple, / for division, + for sum, - for subtraction: ")
    number1 = int(number1)
    number2 = int(number2)
    if operation == "*":
        print(number1 * number2)
    elif operation == "/":
        if number2 == 0:
            print("No division by zero!!!!!!")
        else:
            print(number1 / number2)
    elif operation == "+":
        print(number1 + number2)
    else:
        print(number1 - number2)




