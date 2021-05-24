def isinteger(s):
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()

def isfloat(s):
    a=s.partition('.')
    return  (a[0]=="" and a[2].isdigit()) or (a[0]=="-" and a[2].isdigit()) or (a[0].isdigit() and  a[2].isdigit()) or (isinteger(a[0]) and a[2].isdigit() ) or (a[0].isdigit() and a[2]==0) or (a[0].isdigit() and a[2]=="")

print(isfloat('.112'))
print(isfloat('-.112'))
print(isfloat('3.14'))
print(isfloat('-3.14'))
print(isfloat('5.')) 
print(isfloat('5.0'))
print(isfloat('-.'))
    
