def total_count(n):
    if n%2==1:
        return n+total_count(n-1)
    elif n==0 :
        return 0
    else:
        return total_count(n-1)
a=int(input("Please input the number : "))
print(total_count(a))
    
