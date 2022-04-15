
import functools


def fib(n):
    if n<=1:
        return n
    else:
        return n * fib(n-1)
    
for i,e in enumerate(range(1,500),start=1):
    print(i,fib(e),end="\n")


    