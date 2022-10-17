def multiply(l1):
    
    i=1
    for x in l1:
        i=i*x
    return i

l1 = [int(e) for e in input("enter numbers sep by comma").split(',')]
print("multiply is",multiply(l1)) 