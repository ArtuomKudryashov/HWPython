
# Checking case: True
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("~~~~~~~~~~~~~ case 1 ~~~~~~~~~~~~~~~~~~~~~~")
x = 9
y = 6

print(x > y)
print("~~~~~~~~~~~~~ case 2 ~~~~~~~~~~~~~~~~~~~~~~")
# Checking case: False
x = 4
y = 6

print(x > y)
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

# 3.2 Modify the previous program to return a string value as
#     a print statement like:
#     "10 is greater then 5" Or opposed "2 is less than 4"

# Checking case 1: 10 is greater than 5
print("~~~~~~~~~~~~~ case 1 ~~~~~~~~~~~~~~~~~~~~~~")
x2 = 10
y2 = 5

if x2 > y2:
    print(f'{x2} is greater than {y2}')
else:
    print(f'{x2} is less than {y2}')
print("~~~~~~~~~~~~~ case 2 ~~~~~~~~~~~~~~~~~~~~~~")
# Checking case 2: 2 is less than 4
x2 = 2
y2 = 4

if x2 > y2:
    print(f'{x2} is greater than {y2}')
else:
    print(f'{x2} is less than {y2}')

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

"""
3.3 Modify the previous program to cover the case to compare only positive numbers,
    zero is not included! in case one of the variables is zero return a string value 
    as a print statement like:
    "One or both numbers are not positive, can't proceed with the comparison!"
"""
# Checking case 1: if any number is zero or negative
print("~~~~~~~~~~~~~ case 1 ~~~~~~~~~~~~~~~~~~~~~~")

x3 = 10
y3 = 0  # -1, -2, -3, etc.

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")

# Checking case 2: 10 is greater than 5
print("~~~~~~~~~~~~~ case 2 ~~~~~~~~~~~~~~~~~~~~~~")
x3 = 10
y3 = 5

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")


# Checking case 3: 2 is less than 4
print("~~~~~~~~~~~~~ case 3 ~~~~~~~~~~~~~~~~~~~~~~")
x3 = 2
y3 = 4

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")

# 3.1 Write a program to return a boolean value as a print statement
#     if one number is greater than another.
#     E.g. If X is greater than Y return True otherwise return False


# Checking case: True
x = 9
y = 6

print(x > y)

# ----------------------------------------------------------------------------
# Checking case: False
x = 4
y = 6

print(x > y)

"""
3.2 Modify the previous program to return a string value as 
    a print statement like: 
    "10 is greater then 5" Or opposed "2 is less than 4"
"""
# Checking case 1: 10 is greater than 5
x2 = 10
y2 = 5

if x2 > y2:
    print(f'{x2} is greater than {y2}')
else:
    print(f'{x2} is less than {y2}')

# ----------------------------------------------------------------------------
# Checking case 2: 2 is less than 4
x2 = 2
y2 = 4

if x2 > y2:
    print(f'{x2} is greater than {y2}')
else:
    print(f'{x2} is less than {y2}')

"""
3.3 Modify the previous program to cover the case to compare only positive numbers,
    zero is not included! in case one of the variables is zero return a string value 
    as a print statement like:
    "One or both numbers are not positive, can't proceed with the comparison!"
"""
# Checking case 1: if any number is zero or negative
x3 = 10
y3 = 0  # -1, -2, -3, etc.

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")

# ----------------------------------------------------------------------------
# Checking case 2: 10 is greater than 5
x3 = 10
y3 = 5

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")

# ----------------------------------------------------------------------------
# Checking case 3: 2 is less than 4
x3 = 2
y3 = 4

if (x3 > 0) and (y3 > 0):
    if x3 > y3:
        print(f'{x3} is greater than {y3}')
    else:
        print(f'{x3} is less than {y3}')
else:
    print("One or both numbers are not positive, "
          "can't proceed with the comparison!")

# Checking case: True
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Task # 1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print("~~~~~~~~~~~~~ case 1 ~~~~~~~~~~~~~~~~~~~~~~")
x = 9
y = 6

print(x > y)
print("~~~~~~~~~~~~~ case 2 ~~~~~~~~~~~~~~~~~~~~~~")
# Checking case: False
x = 4
y = 6

print(x > y)
