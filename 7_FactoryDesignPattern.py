#Factory Desing Pattern
from abc import ABCMeta,abstractstaticmethod

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        """ Interface Method """
        
class Student(IPerson):
    def __init__(self):
        self.name="Basic Student Name"
        
    def person_method(self):
        print("I am a student")
        
        
class Teacher(IPerson):
    def __init__(self):
        self.name="Basic Teacher Name"
        
    def person_method(self):
        print("I am a teacher")
  
'''      
s1=Student()
s1.person_method()

t1=Teacher()
t1.person_method()
'''

class PersonFactory:
    
    @staticmethod
    def build_person(person_type):
        if person_type=="Student":
            return Student()
        if person_type=="Teacher":
            return Teacher()
        print("Invalid Type")
        return -1
        
if __name__=="__main__":
    choice=input("What type of person do you want to create?\n")
    person=PersonFactory.build_person(choice)
    person.person_method()
        
