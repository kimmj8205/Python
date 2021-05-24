def qsort(s):
    if len(s)>1:
        pivot=s[0]
        (left,right)=partition(pivot,s[1:])
        print(left+[pivot]+right)
        return qsort(left)+[pivot]+qsort(right)
    else:
        return s

def partition(pivot,s):
    left,right=[],[]
    for x in s:
        if x<=pivot:
            left.append(x)
            print('L',left)
        else:
            right.append(x)
            print('R',right)
    return left,right

import random
originlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(originlist)
print(originlist)
afterlist=qsort(originlist)
print(afterlist)
