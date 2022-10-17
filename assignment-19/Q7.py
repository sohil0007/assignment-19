def add(l1):
    
    s = sum(l1)
    return s

l1 = [int(e) for e in input("enter numbers sep by comma").split(',')]    

print("sum is",add(l1))    