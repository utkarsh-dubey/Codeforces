from copy import deepcopy

t=int(input())

for T in range(t):

    n=int(input())
    a=list(map(int,input().split()))

    amin=[]
    amax=[]
    b=deepcopy(a)


    for i in range(5):
        temp=max(a)

        amax.append(temp)
        a.remove(temp)

        temp=min(b)
        amin.append(temp)
        b.remove(temp)


    amax.sort()
    amin.sort()
    # print(amax)
    # print(amin)
    if(amin==amax):
        print(amax[0]*amax[1]*amax[2]*amax[3]*amax[4])
    else:
        one=amin[0]*amin[1]*amin[2]*amin[3]*amax[4]
        # print(amin[0],amin[1],amin[2],amin[1],amax[4])
        two=amin[0]*amin[1]*amax[4]*amax[3]*amax[2]
        three=amax[4]*amax[3]*amax[2]*amax[1]*amax[0]
        # print(one,two,three)
        print(max(one,two,three))
