def max_sort(s):
    n=len(s)
    ss=[]
    for i in range(n):
        if s!=[]:
            m=max(s)
            s.remove(m)
            ss.append(m)
    return ss
        

import random
random_list = [random.randint(1,100) for i in range(30)]
print('The origin list is',random_list)
sort_list = max_sort(random_list)
print('The sorted list is',sort_list)
