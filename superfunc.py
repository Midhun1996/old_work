
class Base:
    def __init__(self):
        print("Base__init__")
        
class Child1(Base):
    def __init__(self):
        super().__init__()
        print("Child1.__init__")
        
class Child2(Base):
    def __init__(self):
        super().__init__()
        print("Child2.__init__")
        
class Child3(Child1,Child2):
    def __init__(self):
        super().__init__()
        print("Child3.__init__")
        
ch3 = Child3()

print(Child3.__mro__)