t=int(input())

for T in range(t):

    n=int(input())

    ymax=10**5
    xmax=10**5
    ymin=-1*(10**5)
    xmin=-1*(10**5)

    for i in range(n):
        a=list(map(int,input().split()))
        if(a[2]==0):
            xmin=max(xmin,a[0])
        if (a[3] == 0):
            ymax = min(ymax, a[1])
        if (a[4] == 0):
            xmax = min(xmax, a[0])
        if (a[5] == 0):
            ymin = max(ymin, a[1])

    if(xmin<=xmax and ymax>=ymin):
        print(1,xmax,ymax)
    else:
        print(0)


