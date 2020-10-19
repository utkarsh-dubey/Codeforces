a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())



num=0

while((a>0 and d>0) or (b>0 and c>0 and d>0)):

	if((e>f or (b<=0 or c<=0 or d<=0)) and ( a>0 and d>0)):
		num+=e
		a-=1
		d-=1
	elif(b>0 and c>0 and d>0):
		num+=f
		b-=1
		c-=1
		d-=1


print(num)

