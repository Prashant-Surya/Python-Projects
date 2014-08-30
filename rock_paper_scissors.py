from random import randint
c=0
p=0
print("Select exit to exit from game")
while True:
    s=input("Select rock,paper or scissors: ").lower()
    if s=='rock':
        a=0
    elif s=='paper':
        a=1
    elif s=='scissors':
        a=2
    elif s=='exit':
        print("You chose to exit")
        break
    else:
        print("Enter a valid choice")
        continue
    if a in [0,1,2]:
        print("Your Choice is",s)
    b=randint(0,2)
    if b==0:
        print("Computer's choice is rock")
    elif b==1:
        print("Computer's choice is paper")
    elif b==2:
        print("Computer's choice is scissors")
    if a==b:
        print("Tie")
    elif a==0:
        if b==1:
            print("Computer Wins")
            c+=1
        elif b==2:
            print("Player wins")
            p+=1
    elif a==1:
        if b==0:
            print("Player wins")
            p+=1
        elif b==2:
            print("Computer Wins")
            c+=1
    elif a==2:
        if b==0:
            print("Computer Wins")
            c+=1
        elif b==1:
            print("Player wins")
            p+=1
    print("Computer Wins "+str(c)+" Player Wins "+str(p))
            
