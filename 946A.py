n=int(input())
a=list(map(int,input().split()))

b=[]
c=[]
sum1=0
sum2=0
for i in a:
    if(i>=0):
        sum1+=i
    else:
        sum2+=i

print(sum1-sum2)