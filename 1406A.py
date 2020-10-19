t=int(input())

for T in range(t):

    n=int(input())
    a=list(map(int,input().split()))
    first=0
    second=0

    amin=min(a)
    amax=max(a)

    if(amin!=0):
        print(0)
        continue

    else:
        flag=0
        another_flag=0
        # for i in range(102):
        #     if(i>amax):
        #         i-=1
        #         another_flag=1
        #
        #     if i not in a and flag==0:
        #         first=i;
        #         flag+=1
        #     if a.count(i)==1 and flag==0:
        #         first=i
        #         flag+=1
        #
        #
        #     if i not in a and flag==1 and (first!=i or another_flag==1):
        #         second=i
        #         flag+=1
        #     # if a.count(i)<=1 and flag==1 and first!=i:
        #     #     second=i
        #     #     flag+=1
        #     if flag==2:
        #         break
        for i in range(102):
            if i not in a:
                first=i;
                break

        for i in range(102):
            if a.count(i)<=1:
                second=i;
                break

        print(first+second)

