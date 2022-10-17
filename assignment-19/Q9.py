def test_range(n):
    
    if n in  range(1,10):
        print(n,"is in the range")

    else:
        print(n,"is outside the range")

n = int(input("enter value:"))
test_range(n)            