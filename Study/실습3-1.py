def score_average():
    print('i wlll cal avg Score')
    count=0
    total=0
    while True:
        a=input("score :")
        while not a.isdigit():
            a=input("score again :")
        a=int(a)
        if a==0:
            break
        else:
            count=count+1
            total=total+a
    if total==0:
        print( "there is no score")
    else:
        print("avg score of" ,count, 'sub(s) is ', round(total/count,1))
