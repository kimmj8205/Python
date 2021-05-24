def inchmeter():
    while True:
        a=input("type(i/m) :")
        while not (a=='m' or  a=='i') :
            a=input("right type(i/m) :")
        b=int(input("length :"))
        if a=='i':
            print(float(b)*0.0254)
        else:
            print(float(b)*39.37007874015748)
        c=input("continue?(y/n)")
        if c=='n':
            break
    print("the end")
          
