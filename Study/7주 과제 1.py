def find_number(s):
    key=int(input("Number :"))
    for i in s:
        if i == key:
            s.append(0)
            return s
        
    s.append(1)
    return s

def create_file(s):
    t=open('out.txt','w')
    for i in s:
        i=str(i)
        t.write(i)
        t.write('\n')
    t.close()

import random
random_list=[random.randint(1,100) for i in range(30)]
print('The origin list is', random_list)
find_list=find_number(random_list)
print('The result of the first stage :',find_list)
create_file(find_list)
