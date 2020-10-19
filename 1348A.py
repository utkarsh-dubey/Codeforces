t=int(input())
for T in range(t):

    n=int(input())
    sum1=2**n
    sum2=2**(n-1)
    for i in range((n-2)//2):
        if(sum1>=sum2):
            sum1+=2**(i+1)
            sum2+=2**(n-2-i)

    print(abs(sum1-sum2))