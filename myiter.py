

class MyIter:
    
    def __init__(self,start,stop,step=1):
        self.start = start
        self.stop = stop
        self.step = step
        
    def __iter__(self):
        self.prtv = None
        return self
    
    
    def __next__(self):
        while self.start<self.stop:
            self.prtv = self.start
            self.start += self.step
            return self.prtv
        else:
            raise StopIteration
        
iter1 = MyIter(1,10,2)

for e in iter1:
    print(e)