def fibo(n):
    bunny,rabby=1,0
    for _ in range(2,n+1):
        bunny,rabby=rabby,bunny+rabby
    return bunny+rabby
