lst=[20,30,40,234]
print("type(lst)",type(lst))
b=bytes(lst)
print("type(b)",type(b))
#b[3]=22

b1=bytearray(lst)
print("type(b1)",type(b1))
b1[2]=33
