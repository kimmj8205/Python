def exfor():
    a=input(':')
    while not a.isdigit():
        a=input(':')
    a=int(a)
    for i in range(1,1+a):
        if i%5==0:
            print("Likey")
        else:
            print("Like")
exfor()
