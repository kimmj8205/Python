def bubble():
    a=int(input("a"))
    b=int(input("b"))
    c=int(input("c"))
    d=int(input("d"))
    e=int(input("e"))
    l=[a,b,c,d,e]
    n=len(l)
    for i in range(n-1):
        print(l, "1")
        for j in range(n-1):
            if l[j]>l[j+1]:
                c=l[j]
                l[j]=l[j+1]
                l[j+1]=c
                print(l, "2")
            else:
                print(l, "3")
    print(l)
bubble()
                
