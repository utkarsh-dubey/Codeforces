n=int(input())


req=[4,8,15,16,23,42]
check=[0,0,0,0,0,0]
num=[0,0,0,0,0,0]

a=list(map(int,input().split()))

for i in a:

    ind=req.index(i)
    if(ind==0):
        check[0]=1
        num[0]+=1
    elif(num[ind-1]):
        # if(num[ind-1]==1):
        #     check[ind-1]=0
        # else:
        #     check[ind-1]=1
        num[ind-1]-=1
        num[ind]+=1

print(n-num[5]*6)