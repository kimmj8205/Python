def fac1():
    a=input("Number : ")
    while not a.isdigit():
        a=input("Number again : ")
    a=int(a)
    n=1
    while a!=1:
        n=n*a
        a=a-1     
    print(n)

def fac2(n):
    b=1
    m=n
    for i in range(1,m):
        b=b*n
        n=n-1
    print(b)

def fac3(n):
    if n>0:
        return n*fac3(n-1)
    else:
        return 1
        
    
    
    
