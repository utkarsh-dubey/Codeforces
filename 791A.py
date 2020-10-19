n,k=map(int,input().split())
i=0
while(i>=0):
    n*=3
    k*=2
    i+=1
    if(n>k):
        print(i)
        break
        
        