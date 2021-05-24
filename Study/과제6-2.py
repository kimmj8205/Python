def bubble_sort(olist):
    n=len(olist)
    for i in range(n-1):
        for j in range(n-1-i):
            if olist[j] > olist[j+1]:
                a=olist[j]
                olist[j]=olist[j+1]
                olist[j+1]=a
    return olist
    
import random
originlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(originlist)
print(originlist)
afterlist=bubble_sort(originlist)
print(afterlist)
