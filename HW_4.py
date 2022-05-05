print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 4.1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 4.1 Write a program to print result like (use loop):
#     H
#     e
#     l
#     l
#     o
#
#     P
#     y
#     t
#     h
#     o
#     n
#     !
# """
for letter in "Hello Python!":
    print(letter)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 4.2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 4.2 Write a program that uses loop and prints numbers from 1 to 100
#     but the program should stop if a number is equal to 45.


i = 1
while i <= 100:
    print(i)
    if i == 45:
        break
    i += 1
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 4.3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 4.3 Write a program that prints even numbers from 1 to 20.

for i in range(1, 21):
    if (i % 2) == 0:
        print(i)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 4.4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 4.4 Write a program that prints odd numbers from 1 to 30.

for i in range (1,30):
    if (i % 2)==1:
        print(i)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 4.5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# 4.5 Write a program that prints first 10 letters from ABC, the results should be like:
#     1 a
#     2 b
#     3 c
#     4 d
#     5 e
#     6 f
#     7 g
#     8 h
#     9 i
#     10 j
abc = "abcdefghij"
for i in  range (1, 11):
    print(i, abc[i - 1])

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 4.6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# ?4.6 Write a program that prints numbers from 30 to 0 in decreasing order.

for i in range(30, -1, -1):
    print(i)

