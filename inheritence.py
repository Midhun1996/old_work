class Employee:
    up_raisal = 1.25
    
    def __init__(self,name,city,pay):
        self.name = name
        self.city = city
        self.pay = pay
        
    def wagerevision(self):
        self.pay = int(Employee.up_raisal * self.pay)
        return self.pay
    
class Developer(Employee):
    up_raisal = 1.10


d1 = Developer("Midhun","Trichy",50000)
d2 = Developer("Chandra Mohan","Trichy",75000)

print(d1.pay)
d1.wagerevision()
print(d1.pay)