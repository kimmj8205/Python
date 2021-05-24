def file_read():
    t=open('result.txt','r')
    s=t.readlines()
    t.close()
    return s
def bub_sort(s):
    for i in range(len(s)):
        a=s[i]
        if len(a)==2:
            s[i]=a[:2]
            b=s[i]
            s[i]=int(b)
        elif len(a)==3:
            s[i]=a[:3]
            b=s[i]
            s[i]=int(b)
        else:
            s[i]=a[:4]
            b=s[i]
            s[i]=int(b)
    for i in range(len(s)-1):
        for j in range(len(s)-1-i):
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
    return s                  
def find_number(s):
    k=int(input('key :'))
    for i in range(len(s)):
        if k==int(s[i]):
            print("Found!")
            return
    for i in range(len(s)-1):
        if abs(int(s[i])-k) < abs(int(s[i+1])-k):
            print(s[i])
            return
        elif abs(int(s[i])-k) == abs(int(s[i+1])-k):
            if s[i]!=s[i+1]:
                print(s[i],' ',s[i+1])
                return
        elif k>=s[len(s)-1]:
            print(s[len(s)-1])
            return
    print(s[-1])
        
#
first_list = file_read()
print("The list of the 1st stage :",first_list)
second_list=bub_sort(first_list)
print("The list of the 2nd stage :",second_list)
find_number(second_list)
