def length_input():
    l=input("Please enter a length :")
    while not l.isdigit():
        l=input("Please enter a right length :")
    return l
def inchmeter():
    while True:
        b=str(input("Please enter a type : (i/m)"))
        while not(b=='i' or b=='m'):
            b=str(input("Please enter a right type : (i/m)"))
        l=length_input()
        if b=='i':
            a=float(l)*0.0254
            print("It is ", a," meter")
        else:
            a=float(l)*39.37007874015748
            print("It is ", a," inch")
        cont=input("Do you want to continue ? :(y/n)")
        while not(cont=='y' or cont=='n'):
            cont=input("Do you want to continue ? :(y/n)")
        if cont=='n':
            break
    print("The end")
inchmeter()
