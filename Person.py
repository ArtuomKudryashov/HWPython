class Person:
    def __init__(self, name, dob, heigh, gender):
        self.name = name
        self.__dob = dob
        self.height = heigh
        self.gendrer = gender


    def get_name(self):

        return self.name

    def get_dob(self):
        return self.__dob


    def set_dob(self, new_dob):
        self.__dob=new_dob
person_one = Person ("John", "May 1 2000",6, "M")
print((person_one.get_name()))
print (person_one.get_dob())
person_one.set_dob("May 1 , 2000")
print(person_one.get_dob())