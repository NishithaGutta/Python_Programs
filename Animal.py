class Animal:
    def __init__(self,t):
        self.type = t   # constructor assigns value
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
# create object
a1 = Animal("car")
# access variable and methods
print("Type:", a1.type)
a1.eat()
a1.sleep()
