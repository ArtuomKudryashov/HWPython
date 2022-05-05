




def task(a):
    ll="<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    rl=">>>>>>>>>>>>>>>>>>>>>>>>>>>"
    task = "Задача №"
    print(ll,task,a,rl)


def cas(b):
    ll="~~~~~~~~~~~~~~~~~~~~~~~~~~"
    rl="~~~~~~~~~~~~~~~~~~~~~~~~~~"
    cas = "Case №"
    print(ll,cas,b,rl)
task(6)
cas(1)
def print_entities(list):
    for item in list:
        print(item)

# Checking case 1: print_entities(["a", "b", "c"])
print_entities(["a", "b", "c"])


def func (param):
    param.append(0)

a = [10,20]
b = [30.40]
func(a)
func(b)
print(a)
print(b)





task(6)
cas(2)


def convert_string_to_tuple(text):
    new_list =[]
    for item in text:
        new_list.append(item)
    return tuple(new_list)

    # Checking case 1: convert("abide") should return tuple ("a", "b", "i", "d", "e")
print(convert_string_to_tuple("abide"))

task(6)
cas(2)
def conv(text):
    new_list1 =[]
    for item in text:
        new_list1.append(item)
    return tuple(new_list1)



print(conv( "abide" ))
print(convert_string_to_tuple ("abide"))

task(6)
cas(3)
def remove_dups(text):
    return list(set(text))
print(remove_dups("abcdadab"))


# 6.4 Write a program/function that collects certain data as parameters and returns a dictionary object.
#     e.g. client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261")
#     should return a dictionary object like:
#         {
#             "Name": "John",
#             "Lastname": "Doe",
#             "DOB": "01/23/1934",
#             "Sex": "Male",
#             "City": "San Antonio",
#             "State": "TX",
#             "ZipCode": "78261"
#         # }
def create_client_object(name, last_name, dob, sex, city, state, zip_code):
    client = {
        "Name": name,
        "LastName": last_name,
        "DOB": dob,
        "Sex": sex,
        "City": city,
        "State": state,
        "ZipCode": zip_code
    }
    return client

c= create_client_object("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261")
print(c)



