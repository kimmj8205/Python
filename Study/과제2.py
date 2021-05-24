def mult(m,n):
    def loop(n,sum):
        if n>0:
            return loop(n-1,m+sum)
        else:
            return sum
    sum=loop(n,0)
    print(sum)

a=int(input("1st :"))
b=int(input("2nd :"))
mult(a,b)
