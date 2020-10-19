n=int(input())
a=str(input())
b=str(input())
one=0
two=0
three=0
four=0

for i in range(n):
    if(a[i]=='0' and b[i]=='0'):
        one+=1
    elif(a[i]=='0' and b[i]=='1'):
        two+=1
    elif(a[i]=='1' and b[i]=='0'):
        three+=1
    else:
        four+=1

# print(one,two,three,four)
print(one*four+two*three+one*three)
