
class A:
    var = "class variable"
    # __slots__ = ('x','y','z','__dict__')
    __slots__ = ('x','y','z')
    
    def __init__(self,x=None,y=None,z=None):
        self.x = x
        self.y = y
        self.z = z
        
a1 = A()
A.new_var = "new_var"
# a1.k = 20
print(a1.__slots__)
print(A.__dict__)

