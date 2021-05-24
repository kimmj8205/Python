def find_number(s):
    n=int(input("Key :"))
    for i in range(len(s)):
        if s[i]==n:
            s.append(0)
            return s
    s.append(1)
    return s
def create_file(s):
    t=open('result.txt','w')
    for i in range(len(s)):
        k=str(s[i])
        t.write(k)
        t.write('\n')
    t.close()
import random
random_list=[random.randint(1,100) for i in range(30)]
print("The origin list is", random_list)
find_list = find_number(random_list)
print("The result of the first stage :",find_list)
create_file(find_list)
