class Class1(object):
    def __init__(self):
        print("Class1")
        
    def __str__(self):
        return "This is class1"        
class Class2(object):
    def __init__(self):
        print("Class2")
        
    def __str__(self):
        return "This is class2"        
class Class3(Class2, Class1):
    def __init__(self):
        Class1.__init__(self)
        Class2.__init__(self)
        print("Derived")
          
    def __str__(self):
        return "This is class3"


c= Class3()
print(c)