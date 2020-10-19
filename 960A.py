s=str(input())

a=0
b=0
c=0
flag=False
flag2=False
for i in s:
    if(i=='a'):
        if(flag or flag2):
            print("NO")
            exit(0)
        a+=1
    elif(i=='b'):
        flag=True
        if(flag2):
            print("NO")
            exit(0)
        b+=1
    else:
        flag2=True
        c+=1
    if(a==0 and (b!=0 or c!=0)):
        print("NO")
        exit(0)
    if(b==0 and c!=0):
        print("NO")
        exit(0)

if((a==c or b==c) and a!=0 and b!=0 and c!=0 ):
    print("YES")
else:
    print("NO")
