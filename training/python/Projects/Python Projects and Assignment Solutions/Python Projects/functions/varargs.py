import math
def add(*x):
    print(x)
    print(type(x))
    print("Sum is", math.fsum(x))
    
print(add(20,30,40))