def score_average():
    print('i wlll cal avg Score')
    count=0
    total=0
    fail=0
    while True:
        a=input("score :")
        while not a.isdigit():
            a=input("score again :")
        a=int(a)
        if a==0:
            break
        else:
            if a>=60:
                count=count+1
                total=total+a
            else:
                fail=fail+1
    if total==0:
        if fail==0:
            print( "there is no score")
        else:
            print("you failed" ,fail,"sub(s)")
            
    else:
        print("avg score of" ,count, 'sub(s) is ', round(total/count,1))
        print("you failed" ,fail,"sub(s)")
