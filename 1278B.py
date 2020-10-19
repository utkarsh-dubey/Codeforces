n=int(input())

for i in range(n):
    
    x,y=map(int,input().split())
    
    a=min(x,y)
    b=max(x,y)
    
    k=int((-1+(1+4*((b-a)*2))**0.5)/2)
    
    if ((b-a)%2==0):
        
        while True:
            if (k**2+k)%4==0 and ((k**2+k)//2-(b-a))>=0:
                print (k)
                break
            k+=1
    else:
        
        while True:
            if (k**2+k)%4==2 and ((k**2+k)//2-(b-a))>=0:
                print (k)
                break
            k+=1
    
    