n=int(input())

l="I love"
h="I hate"

for i in range(n):
    
    if(i%2==0):
        print(h,end='')
    elif(i%2!=0):
        print(l,end='')
     
    if(i!=n-1):   
        print(' that ',end='')
    
print(" it",end='')