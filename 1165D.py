t=int(input())

for T in range(t):

    n=int(input())
    a=list(map(int,input().split()))
    check=set(a)
    temp=set()
    guess=min(a)*max(a)
    guesscheck=2
    while(guesscheck*guesscheck<=guess):

        if(guess%guesscheck==0):
            temp.add(guesscheck)
            temp.add(guess/guesscheck)
        guesscheck+=1

    if(temp==check):
        print(guess)
    else:
        print(-1)