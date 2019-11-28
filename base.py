import dice

def playgame(player1, player2):
    roundCtr=0
    scoreP1 = 0
    scoreP2 = 0
    
    
    while roundCtr < 5:
        input(player1 + " press enter")
        score = dice.twoRolls()
        scoreP1 += score
        print (player1, "score " , score, scoreP1)

        input(player2 + " press enter")
        score = dice.twoRolls()
        scoreP2 += score
        print (player2, "score " , score, scoreP2)
        roundCtr += 1 


    if (scoreP1 < scoreP2):
        print(player2, "winner")
        #score
        winnername=player2
        winnerscore=scoreP2
        
    elif scoreP1 > scoreP2:
        print(player1, "winner")    
        # score
        winnername=player1
        winnerscore=scoreP1
     
     
    else:
        # if scoreP2==scoreP1
        ## then its sudden death
        scoreDeathP1=0
        scoreDeathP2=0
        while scoreDeathP1==scoreDeathP2:
            input(player1, "press enter")
            scoreDeathP1=dice.dice()
            print(scoreDeathP1)
            input(player2, "press enter")
            scoreDeathP2=dice.dice()
            print(scoreDeathP2)   
        
        if scoreDeathP1<scoreDeathP2:
            print(player2, "winner")
            winnername=player2
            winnerscore=scoreP2
            
        elif scoreDeathP1>scoreDeathP2:
            print(player1, "winner")    
            winnername=player1
            winnerscore=scoreP1
        
    return(winnername, winnerscore)


player1_global=input("Enter name, player 1: ")
player2_global=input("Enter name, player 2: ")

result = playgame(player1_global, player2_global)

print("winner name", result[0],"winner score", result[1])

    


    