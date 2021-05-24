def msort0(s):
    if len(s)>1:
        mid =len(s)//2
        return merge0(msort0(s[:mid]),msort0(s[mid:]))
    else:
        return s

def merge0(left,right):
    if not ((left==[]) or (right==[])):
        if left[0]<=right[0]:
            return[left[0]]+merge0(left[1:],right)
        else:
            return [right[0]]+merge0(left,right[1:])
    else:
        return left+right
                                     
import random
originlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
random.shuffle(originlist)
print(originlist)
afterlist=msort0(originlist)
print(afterlist)
