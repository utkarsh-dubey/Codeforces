t=int(input())
for _ in range(t):
    n=int(input())
    if(n==1):
        print(-1)
    else:
        print("2",end="")
        for i in range(n-1):
            print("3",end="")
        print()