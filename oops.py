#so basically this pyhton code file cover all the code for oops concept i have made notes in this file mentioned as comments
#you can view this file to get overview of the concept oops 

a = 12
b= 43
print(a+b)
#oops apporach advantages
#multiple usuage 
#security
#for management 

#classes - blueprint,varibake is attribute in class,function is method 
#
class Factory:
    a = 12
    #def hello(self): #method
        #print("how are you")
    #print("hello how are you")

#print(Factory().a)
#Factory().hello() 


#OBJECTS - 
obj = Factory()

print(obj.a)

#obj.hello()

#what is self in the above function and what is the connection 
#object and class

#constructor - with constructor we can ask a user for parameter

# class Vasu:
#     def __init__(self,material,pockets,zips):
#         self.material = material
#         self.pockets = pockets
#         self.zips = zips

# reebok = Vasu("leather",3,2)
# # now reebok has all the access in the factory class
# print(reebok.pockets)
# #in above example you get to know that you can store a lot of data in one class
# #and can get access this means you dont have to store the same data multipile time

# def show(self):
#     print(f"your material are")

# #type of Attribute & Method 


# class Animal:
#     name= "lion" #class attribute 
    
#     def __init__(self,age):
#         self.age = age #instance attribute

#     def showw(self):
#         print(f"how are you and your age is {self.age}")
#     #this is a class method
#     @classmethod
#     def helloa(cls):
#         print("how are you brother")
#     @staticmethod
#     def static():
#         print("How are you")
# obj = Animal(12)

# obj.showw()

# obj.static()


# #IMPORTANT NOTES
# #4 PILLAR OF OOPS

# #1 INHERITANCE
# class Factory:
#     a = "I am an attribute mentioned inside"
#     def hello(self):
#         print("hello I am  a method metioned inside factory")

# class Factorypune(Factory):
#     pass

# obj1 = Factory()

# obj2 = Factorypune()

# class Human(Factory):
#     pass

# class Animal:
#     def hello(self,name):
#         self.name = name

# personal = Animal("vasu")
# #basically a super() in above line of code is used to access the Parent class so that we dont need to call it again and again 
# class animal2(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age


# #types of inheritance 
# class Animal:
#     name1 = "lion"

# class Human:
#     name2 = "harsh"
# class robots(Animal,Human):
#     name3 = "gaha"
# obj = robots()

# print(obj.name1)


# #basically it is a factory structure 
# #multi level inheritance
# class SearchFactory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class bBhopalFactory(SearchFactory):
#     def __init__(self, material, zips,colour):
#         super().__init__(material, zips)
#         self.colour = colour

# class PuneFactory(bBhopalFactory):
#     def __init__(self, material, zips, colour,pockets):
#         super().__init__(material, zips, colour)
#         self.pockets = pockets

# obj5 = PuneFactory()

#Advanced Python
#decorator - is a function / method which can can modify 
def decorate(func):
    def wrapper():
        print("i will print myself before the function")
        func()
        print("i will print after the function")
    return wrapper
@decorate
def hello1():
    print("hello i am vasu bansal")

l = []
for i in range(1,21):
    if i % 2 ==0:
        l.append(i)

print(l)
l = [i for i in range(1,21) if i % 2==0]

print(l)

#lambda impression
addition = lambda a,b : a+b
print(addition(12,13))

#map filter and zip

a = [1,2,3,4,5]

result = map(lambda x: x*2,a)

print(list(result))

def evenodd(x):
    if x%2==0:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8]

result = filter(evenodd, a)
print(list(result))