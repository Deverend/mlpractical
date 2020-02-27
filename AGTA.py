import numpy as np

# 4 different start value for players
def start_rule(i):
    if i == 0:
        return 0,0
    elif i == 1:
        return 0,1
    elif i == 2:
        return 1,0
    elif i == 3:
        return 1,1

# 4 different tie_breaking rule for players
def tie_breaking_rule(j):
    if j == 0:
        return 0,0
    elif j == 1:
        return 0,1
    elif j == 2:
        return 1,0
    elif j == 3:
        return 1,1

def play(round,i,j):
    k = 0
    i = i
    j = j
    # initialize record for players
    player1_record = [start_rule(i)[0]]
    player2_record = [start_rule(i)[1]]

    while (k<=round):
        #player1 strategy
        if player2_record.count(0)/float(len(player2_record)) == 0.5:
            player1_thisturn = tie_breaking_rule(j)[0]
        if 0.5 < player2_record.count(0)/float(len(player2_record)):
            player1_thisturn = 0
        else:
            player1_thisturn = 1
        #player2 strategy
        if player1_record.count(0)/float(len(player1_record)) == 0.5:
            player2_thisturn = tie_breaking_rule(j)[1]
        if 0.5 < player1_record.count(0)/float(len(player1_record)):
            player2_thisturn = 1
        else:
            player2_thisturn = 0
        #update record
        player1_record.append(player1_thisturn)
        player2_record.append(player2_thisturn)
        k+=1
    return player1_record.count(0)/float(len(player1_record)), player2_record.count(0)/float(len(player2_record))

for i in range(0,4):
    for j in range(0,4):
        print('{},{},{}'.format(i,j,play(10000,i,j)))
