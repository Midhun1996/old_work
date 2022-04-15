
class Bike:
    color = None
    
    
def changecolor(obj,att):
    obj.color = att
    
b1 = Bike()
b2 = Bike()
b3 = Bike()

changecolor(b1,"red")
changecolor(b2,"green")
changecolor(b3,"white")


print(b1.color,
      b2.color,
      b3.color)