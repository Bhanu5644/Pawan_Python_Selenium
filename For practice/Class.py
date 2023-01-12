class DemoClass:
    def Showname(self):
        print("Bhanu")
ko=DemoClass()
ko.Showname()

class DemoClass:
    a=50
    def __int__(self): #Constructor
        print("Munish")
    def ShowValue(self): # Function
        print(self.a)
    def Showvalue1(self):
        print("Bhanu Sharma")

Object = DemoClass() #Call Object
Object.ShowValue()
Object.Showvalue1()

class A:
    def DisplayA(self):
        print("Welcome to India ")
class B:
    def DisplayB(self):
        print("Welcome to rajasthan")
class C(A,B):
    def DisplayC(self):
        print("Not in Huawei")
obj=C()
obj.DisplayA()
obj.DisplayB()
obj.DisplayC()
