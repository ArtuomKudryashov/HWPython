
# pas = input ("Enter  your password :"  )
# confirmation = input ("Enter conf")
# confirmation == pas
# if pas == confirmation:
#     print ("pass")
# else:
#     print("Wrong")
#


# numb = int (input("Число "  ))
# if ( numb/2 ==0):
#     print("is even")
# else:
#     print("is odd")

# numb = int(input("Число "))
# if numb>18:
#     print("Access")
# else:
#     print("Denied")

# massa=int(input())
# high=int(input())
# imt = massa/high**2
# if 18.5<= imt and imt <=25:
#       print ("optimal" )
# elif imt<18.5:
#     print("косяк")
# else:
#     print("Over")

# a = int (input())
# if a > 7:
#     print("Значение бельше ")
# elif a<-3:
#     print("Значение в меньше")
# else:
#     print("Внутри ренджа")
#

# a = int (input())
# if a>-30 and a <=-2 or 7<a and a<=25:
#     print("Belongs")
# else:
#     print("It is in wrong reng")
#
a = int(input())
b = int(input())
c = int(input())

# if a < (b+c) and (b<a+c) and (c< a+b):
#     print("triangle")
#
# else:
#     print("Not triangle")
#
if a==b and a==c and c==b :
    print("Equilateral")
elif a==b or b==c or a==c:
    print ("Isosceles")
else:
    print("Scales")

def more_than_five(lst):
    new_list = []
    for list_element in lst:
        if abs(list_element) > 5:
            new_list.append(abs(list_element))
    # print(new_list)
    return new_list

print(more_than_five([-11, 4, -2, 90, 400, 0, -5]))
print(more_than_five([-2, 2, 3, 4, 0, -1]))
print(more_than_five([70, -900, 41, 0]))











