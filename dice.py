import random
random.seed()


def dice():
    diceVal=random.randrange(1,6)
    return(diceVal)

def twoRolls():
    total = 0
    
    
    r1 = dice()
    r2 = dice()
    r3 = dice()
    total = r1 + r2
    print("Initial roll ", r1, r2, total)


    result = total
    
    if ((total % 2)==0):    ## detect even rolls
        result+=10
        print ("even")
        
    else:                   ## odd toll
        result-=5
    
    if r1==r2:              ## double
        result+=r3
        print("double")
    if result < 0:          ## min score 0
        result=0
 
    #print(result)
    return(result)

    