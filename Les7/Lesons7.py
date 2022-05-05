file = open("text.txt","r") #  ключи x w a file = open("text.txt","r") #  ключи x w a


# print(file.read())
# print(file.readline())    # построчно
# print(file.read(4))    # построчно

# for line in file:
#     print(line)
#
#
# file.close()

# file = open ("test_1.txt", "w") # написать
# file.write("my super texxt")
# file.close()
#
# file = open ("test_1.txt", "r") # читать
# print(file.read())
# file.close()

with open ("test_1.txt", "w") as file:
    file.write("Some dummy text")