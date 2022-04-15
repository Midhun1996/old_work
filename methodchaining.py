
class Car:
    def turnon(self):
        print("The car has started")
        return self

    def drive(self):
        print("The car on the move")
        return self
            
    def brake(self):
        print("The car has stopped")
        return self
            
    def turnoff(self):
        print("The car is turned off")
        return self    

santro = Car()

santro.turnon()\
      .drive()\
      .brake()\
      .turnoff()