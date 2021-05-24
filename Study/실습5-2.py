def mult(m,n):
    def loop(n,sum):
        if n>0:
            return loop(n-1,m+sum)
        else:
            return sum
    sum=loop(n,0)
    print(sum)
mult(3,6)
