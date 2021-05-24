def fibo2(n):
    i=1
    bunny,rabby=1,0
    if n==1:
        return 1
    elif n==0:
        return 0
    while i<n:
        i=i+1
        bunny,rabby=rabby,bunny+rabby
    return bunny+rabby
