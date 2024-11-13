import random

player1_score=0
player2_score=0

while True:
    
    player1=input("nhap vao ki tu(b/d/k): ")
    player2=random.randint(0,2)
    if player2==0:
        print("bao")
    elif player2==1:
        print("da")
    elif player2==2:
        print("keo")
    else:
        print("error")
    if player1=='b':
        if player2==0:
            print("draw")
        elif player2==1:
            print("player 1 win")
            player1_score+=1
        elif player2==2:
            print("player 2 win")
            player2_score+=1
        else:
            print("error")
    elif player1=='d':
        if player2==0:
            print("player 2 win")
            player2_score+=1
        elif player2==1:
            print("draw")
        elif player2==2:
            print("player 1 win")
            player1_score+=1
        else:
            print("error")
    elif player1=='k':
        if player2==0:
            print("player 1 win")
            player1_score+=1
        elif player2==1:
            print("player 2 win")
            player2_score+=1
        elif player2==2:
            print("draw")
        else:
            print("error")
    else:
        print("error")
    print(str(player1_score)+"--"+str(player2_score))
