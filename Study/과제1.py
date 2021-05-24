def total_count(n):
        if n==0:
            return 0
        elif (n%2==1):
            return n+total_count(n-1)
        else :
            return 0+total_count(n-1)

a=int(input("Please input the number : "))
print(total_count(a))
