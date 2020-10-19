t=int(input())

for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    ans=[]

    for j in a:
        if(j not in ans):
            ans.append(j)

    for j in ans:
        print(j,end=" ")

    print()
