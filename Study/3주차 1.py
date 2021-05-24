solo=0
l=[]
while True:
    score=input("Score :")
    while not score.isdigit():
        score=input("Score :")
    score=int(score)
    if score%2!=0:
        solo=solo+score
        l.append(score)
        print(l)
    if score==0:
        break
print(solo)
print(min(l))

