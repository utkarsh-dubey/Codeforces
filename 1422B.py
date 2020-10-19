from collections import deque
from math import ceil

t=int(input())
for T in range(t):
    a=[]
    n,m=map(int,input().split())
    for i in range(n):
        a.append(list(map(int,input().split())))
    sum=[]
    # for i in range((n//2)*(m//2)):
    #     sum.append([])

    for i in range(n//2):
        for j in range(m//2):
            sum.append(sorted([a[i][j],a[i][m-j-1],a[n-1-i][j],a[n-1-i][m-1-j]]))
    finalsum=[]
    finalsum1=[]
    total = 0;
    for i in range(len(sum)):
        # finalsum.append((sum[i][0]+sum[i][1]+sum[i][2]+sum[i][3])//4)
        # finalsum1.append((ceil(sum[i][0] + sum[i][1] + sum[i][2] + sum[i][3]) // 4))
        number=sum[i][len(sum[i])//2]
        for j in sum[i]:
            total+=abs(number-j)


    # print(sum)
    # print(finalsum)
    # for i in range(len(finalsum)):
    #     total+=(min(abs(finalsum[i]-sum[i][0])+abs(finalsum[i]-sum[i][1])+abs(finalsum[i]-sum[i][2])+abs(finalsum[i]-sum[i][3]),abs(finalsum1[i]-sum[i][0])+abs(finalsum1[i]-sum[i][1])+abs(finalsum1[i]-sum[i][2])+abs(finalsum1[i]-sum[i][3])))
    lastsum=0
    lastsum1=0
    # print("check",total)
    # print(total)
    if(n%2!=0):
        # print("chalega")
        for i in range(m//2):
            # if(i!=m//2 and m%2!=0):
            #     lastsum+=a[n//2][i]
            # elif(m%2==0):
            #     lastsum += a[n // 2][i]
            total+=(abs(a[n//2][i]-a[n//2][m-i-1]))



        # # print("lastsum",lastsum)
        # if(m%2!=0):
        #     lastsum//=(m-1)
        # else:
        #     lastsum//=m
        #
        # for i in range(m):
        #     if(i!=m//2 and m%2!=0):
        #         total+=abs(lastsum-a[n//2][i])
        #     elif ( m % 2 == 0):
        #         total += abs(lastsum - a[n // 2][i])


    if(m%2!=0):
        for i in range(n//2):
            # if(i!=n//2 and n%2!=0):
            #     lastsum1 += a[i][m // 2 ]
            # elif(n%2==0):
            #     lastsum1 += a[i][m // 2 ]
            total+=(abs(a[i][m//2]-a[n-1-i][m//2]))
        # if(n%2!=0):
        #
        #     lastsum1 //= (n-1)
        # else:
        #     lastsum1//=n
        #
        # for i in range(n):
        #     if(i!=n//2 and n%2!=0):
        #
        #         total += abs(lastsum1 - a[i][m // 2 ])
        #     elif(n%2==0):
        #
        #         total += abs(lastsum1 - a[i][m // 2 ])


    print(total)











