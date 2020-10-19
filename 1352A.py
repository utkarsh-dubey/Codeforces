t=int(input())

for T in range(t):

    n=str(input())
    num=0
    l=list(n)
    # print(l)
    final=[]
    du=len(l)
    # print(du)
    for i in l:
        if(i!='0'):
            num+=1
            # print(int(i))
            temp=int(i)*(10**(du-1))
            final.append(temp)
        # print(final)
        du-=1

    print(num)
    for j in final:
        print(j,end=" ")

    print()