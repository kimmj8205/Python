
def file_read():
    t=open('out.txt','r')
    a=t.readlines()
    return a

def bub_sort(s):
    for i in range(len(s)):
        a=s[i]
        if len(a)==3:
            s[i]=a[:2]
            b=s[i]
            s[i]=int(b)
        elif len(a)==2:
            s[i]=a[:1]
            b=s[i]
            s[i]=int(b)
        else:
            s[i]=a[:3]
            b=s[i]
            s[i]=int(b)
    
    n=len(s)
    
    for i in range(n-1):
        for j in range(n-1-i):
            if s[j] > s[j+1]:
                a=s[j]
                s[j]=s[j+1]
                s[j+1]=a
    return s

def find_number(s):
    key=int(input('Number :'))
    for i in s:
        if i == key:
            print ('Found!')
            return 
    for i in range(len(s)-1):
        if abs(s[i]-key) == abs(s[i+1]-key):
            if s[i] != s[i+1] :
                print(s[i],s[i+1])
                return
        elif abs(s[i]-key) < abs(s[i+1]-key):
            print(s[i])
            return
        elif s[30]<key:
            print(s[30])
            return
        
first_list=file_read()
print('The list of 1st stage :',first_list)
second_list=bub_sort(first_list)
print('The list of the 2nd stage :',second_list)
find_number(second_list)
