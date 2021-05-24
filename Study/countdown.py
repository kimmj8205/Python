import time
def countdown(n):
    while n>0:
        print(n)
        time.sleep(0.3)
        n=n-1
    print("Go !")
countdown(int(input("Insert sec. :")))
