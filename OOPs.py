# class Student:
#     def __init__(self,name,roll):
#         self.name = name   #self. : signifies difference between various objects
#         self.roll = roll
        
# s1 = Student("Surya",72)
# print(s1.name,s1.roll)
# s2 = Student("Kirri",98)
# print(s2.name,s2.roll)
#################################################
# Attributes: class.attr, obj.attr
# Common for all attributes: Class attribute, converse is for Object attribute
#Eg: 
# class Student:
#     name = "Anunymous"
#     def __init__(self,name,roll):
#         self.name = name 
        
# s1 = Student("Surya",72)
# print(s1.name,s1.roll) # output is Surya
######################################################
# Methods: Functions that belong to objects
# class Student:
#     def __init__(self,name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome, ",self.name)

#     def marks(self):
#         print("Marks obtained: ",self.marks)

# s1 = Student("Surya", 100)
# print(s1.name,s1.marks)
#####################################
# Average of 3 subjects
# class College:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Average marks: ",sum/3)


# s1 = College("Surya",[99,98,97])
# s1.avg()
##########################################
# Static Methods: Denot require self parameter but works at class level
# class Student:
#     @staticmethod # Decorator: Wrap another function in order to extend behaviour of the wapped function, without permanently modifying it
#     def hello():
#         print("Hello everyone!")
# s1 = Student()
# s1.hello()
############################################
# Abstraction: 
# Hiding implementation details of a class and only showing the essential features to the user
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brk = False
#     def start(self):
#         self.acc = True
#         self.clutch = True
#         print("Car Started..")
# s1 = Car()
# s1.start()
###########################################
# Encapsulation: Wrapping data and functions into a single unit (object)
# Transactions of credit,debit and balance checking
# class Account:
#     def __init__(self,name,bal):
#         self.name = name
#         self.bal = bal

#     def debit(self,amount):
#         self.bal -= amount
#         print("Rs.",amount,"Was debited")
#         print("Your current balance is ",self.balance())
    
#     def credit(self,amount):
#         self.bal -= amount
#         print("Rs.",amount,"Credited to your account")
#         print("Your current balance is ",self.balance())
    
#     def balance(self):
#         return self.bal
        
# s1 = Account("Surya",10000)
# s1.debit(2000)
# s1.balance()
###########################################
# del keyword
#del s1.name (syntax)
###########################################
# Inheritance: One class (child) derives the proparties & methods of another (parent)
class Car:
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("Heroo")
car1.start()
