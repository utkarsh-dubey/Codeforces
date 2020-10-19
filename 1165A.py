n,x,y = map(int,input().split())
num=str(input())
num=num[n-x:]
if(num[x-y-1]=='1'):
    print(num.count('1')-1)
else:
    print(num.count('1')+1)





