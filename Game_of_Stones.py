# This is a simulation of a board game "GRA O KRZEMIEŃ".
# The main goal is to create a simulation and check how long (how many rolls of the dice) the game takes.

import random
import numpy as np
import statistics

class player:
    ring = 0                                        # which of 3 rings the player is on
    position = 0                                    # which field on the ring the player is on
    small_stones = 0                                # number of small stones gained
    medium_stones = 0                               # number of medium stones gained
    big_stones = 0                                  # number of big stones gained
    n_tools = [False, False]                        # information if the player has the tools needed to dig in "Niszowa" pit
    f_tools = [False, False, False]                 # information if the player has the tools needed to dig in "Filarowo-komorowa" pit
    k_tools = [False, False, False, False, False]   # information if the player has the tools needed to dig in "Komorowa" pit

class games:
    J = 15                                          # number of small stones in "JAMOWA" pit
    N = [5, 6]                                      # numbers of small and medium stones in "NISZOWA" pit
    F = [6, 4]                                      # numbers of medium and big stones in "FILAROWO-KOMOROWA" pit
    K = 6                                           # number of big stones in "KOMOROWA" pit
    tools = [[0, 0], [0, 0, 0], [0, 0, 0, 0, 0]]    # number of tools to draw

# The board is made of three rings.
# Every player starts in the first smallest ring and walk there in circle until all stones from the first pit are gained.
# Every field of the ring has the information of what action can the player do.
# 0 - empty (nothing happens)
# 1-6 - starting points other for every player
# T - player draws lots of the tools needed to mine in pits.
# J, N, F, K - "JAMOWA", "NISZOWA", "FILAROWO-KOMOROWA", "KOMOROWA" pits
# small stones give 1 point each
# medium stones give 2 points each
# big stones give 3 points each


# setting board
ring1 = [1, 'J', 0, 'T', 'T', 0, 2, 0, 'T', 'J', 0, 'T', 3, 'J', 0, 'T', 'T', 4, 0, 0, 'T', 'J', 'T', 5, 'T', 0,
             'J', 'T', 0, 6, 'J', 'T', 'T', 0]
ring2 = [1, 'N', 0, 0, 'T', 'T', 0, 'N', 2, 'T', 0, 'N', 0, 0, 'T', 'N', 3, 0, 'T', 0, 0, 'N', 'N', 'T', 0, 4, 0,
             'T', 0, 'N', 0, 'T', 'N', 5, 0, 0, 'N', 'N', 'T', 'T', 0, 6, 0, 'T', 0, 'N', 0, 'T', 0, 'N']
ring3 = [1, 0, 'F', 0, 'F', 'T', 0, 'K', 0, 0, 2, 0, 0, 'F', 0, 'T', 0, 'K', 'F', 0, 3, 'K', 'T', 0, 'F', 0, 'T', 0,
             0, 'F', 0, 'K', 0, 4, 0, 0, 'F', 0, 'T', 0, 0, 'K', 'F', 5, 0, 'T', 0, 'F', 0, 0, 'K', 0, 'F', 6, 'T', 'F',
             0, 0, 'K', 'K', 0, 'T', 0, 0, 0, 'F']
board = [ring1, ring2, ring3]

#The procedure of drawing tools:
def chooseTool(i,players,game):
    if (players[i].n_tools[0] == False) or (players[i].n_tools[1] == False):
        p = game.tools[0][0] / (game.tools[0][0] + game.tools[0][1])
        U = np.random.uniform()
        if (U < p) and (players[i].n_tools[0] == False):
            players[i].n_tools[0] = True
            game.tools[0][0] -= 1
        elif (U >= p) and (players[i].n_tools[1] == False):
            players[i].n_tools[1] = True
            game.tools[0][1] -= 1
    elif (players[i].f_tools[0] == False) or (players[i].f_tools[1] == False) or (players[i].f_tools[2] == False):
        p1 = game.tools[1][0] / (game.tools[1][0] + game.tools[1][1] + game.tools[1][2])
        p2 = (game.tools[1][0] + game.tools[1][1]) / (game.tools[1][0] + game.tools[1][1] + game.tools[1][2])
        U = np.random.uniform()
        if (U<p1) and (players[i].f_tools[0] == False):
            players[i].f_tools[0] = True
            game.tools[1][0] -= 1
        elif (U>=p1) and (U<p2) and (players[i].f_tools[1] == False):
            players[i].f_tools[1] = True
            game.tools[1][1] -= 1
        elif (U>=p2) and (players[i].f_tools[2] == False):
            players[i].f_tools[2] = True
            game.tools[1][2] -= 1
    elif (players[i].k_tools[0] == False) or (players[i].k_tools[1] == False) or (players[i].k_tools[2] == False) or (players[i].k_tools[3] == False) or (players[i].k_tools[4] == False):
        p1 = game.tools[2][0] / (game.tools[2][0] + game.tools[2][1] + game.tools[2][2] + game.tools[2][3] + game.tools[2][4])
        p2 = (game.tools[2][0] + game.tools[2][1]) / (game.tools[2][0] + game.tools[2][1] + game.tools[2][2] + game.tools[2][3] + game.tools[2][4])
        p3 = (game.tools[2][0] + game.tools[2][1] + game.tools[2][2]) / (game.tools[2][0] + game.tools[2][1] + game.tools[2][2] + game.tools[2][3] + game.tools[2][4])
        p4 = (game.tools[2][0] + game.tools[2][1] + game.tools[2][2] + game.tools[2][3]) / (game.tools[2][0] + game.tools[2][1] + game.tools[2][2] + game.tools[2][3] + game.tools[2][4])
        U = np.random.uniform()
        if (U<p1) and (players[i].k_tools[0] == False):
            players[i].k_tools[0] = True
            game.tools[2][0] -= 1
        elif (U>=p1) and (U<p2) and (players[i].k_tools[1] == False):
            players[i].k_tools[1] = True
            game.tools[2][1] -= 1
        elif (U >= p2) and (U < p3) and (players[i].k_tools[2] == False):
            players[i].k_tools[2] = True
            game.tools[2][2] -= 1
        elif (U>=p3) and (U<p4) and (players[i].k_tools[3] == False):
            players[i].k_tools[3] = True
            game.tools[2][3] -= 1
        elif (U>=p4) and (players[i].k_tools[4] == False):
            players[i].k_tools[4] = True
            game.tools[2][4] -= 1

# The procedure of deciding what the player do after standing on the area:
def check(i,players,game):
    position = players[i].position
    ring = players[i].ring
    if board[ring][position] == 'J':
        players[i].small_stones += 1
        game.J -= 1
    elif (board[ring][position] == 'N') and (players[i].n_tools == [True,True]):
        if (game.N[0]>0) and (game.N[1]>0):
            p = game.N[0] / (game.N[0] + game.N[1])
            U = np.random.uniform()
            if U<p:
                players[i].small_stones += 1
                game.N[0] -= 1
            else:
                players[i].medium_stones += 1
                game.N[1] -= 1
        elif game.N[0]>0:
            players[i].small_stones += 1
            game.N[0] -= 1
        elif game.N[1]>0:
            players[i].medium_stones += 1
            game.N[1] -= 1
    elif (board[ring][position] == 'F') and (players[i].f_tools == [True,True,True]):
        if (game.F[0] > 0) and (game.F[1] > 0):
            p = game.F[0] / (game.F[0] + game.F[1])
            U = np.random.uniform()
            if U<p:
                players[i].medium_stones += 1
                game.F[0] -= 1
            else:
                players[i].big_stones += 1
                game.F[1] -= 1
        elif game.F[0] > 0:
            players[i].medium_stones += 1
            game.F[0] -= 1
        elif game.F[1] > 0:
            players[i].big_stones += 1
            game.F[1] -= 1
    elif (board[ring][position] == 'K') and (players[i].k_tools == [True,True,True,True,True]):
        players[i].big_stones += 1
        game.K -= 1
    elif board[ring][position] == 'T':
        chooseTool(i,players,game)

#move of the player
def move(i,players,game):
    r = random.choice([1,2,3,4,5,6])
    players[i].position = (players[i].position + r) % len(board[players[i].ring])
    check(i,players,game)

# Checking, who won:
def result():
    P=[]
    for i in range(k):
        P.append(players[i].small_stones + ( 2 * players[i].medium_stones) + (3 * players[i].big_stones))
    print("Wygrał gracz numer ",P.index(max(P)),"!" )

# The procedure of one play:
def play(k):
    n=0
    game = games()
    game.N = [5,6]
    game.F = [6,4]
    game.tools = [[k, k], [k, k, k], [k, k, k, k, k]]
    players = []
    for i in range(k):
        players.append(player())
        players[i].position = board[0].index(i+1)
        players[i].n_tools = [False, False]
        players[i].f_tools = [False, False, False]
        players[i].k_tools = [False, False, False, False, False]

    while game.J>0:
        for i in range(k):
            move(i,players,game)
            n += 1

    while (game.N[0]>0) or (game.N[1]>0):
        for i in range(k):
            if players[i].n_tools == [True,True]:
                players[i].ring = 1
                players[i].position = board[1].index(i+1)
            move(i,players,game)
            n += 1

    while (game.F[0]>0) or (game.F[1]>0):
        for i in range(k):
            if players[i].f_tools== [True,True,True]:
                players[i].ring = 2
                players[i].position = board[2].index(i+1)
            move(i,players,game)
            n += 1

    while game.K>0:
        for i in range(k):
            move(i,players,game)
            n += 1
    n += 2 * k

    return n

#checking the mean, min and max number of rolls needed to finish the game from 10000 games for each number of players.
k = 2
results = []
for i in range(10000):
    results.append(play(k))
print("Dla ", k, " graczy:")
print("Średnia: ", statistics.mean(results), ". Minimum: ", min(results), ". Maximum: ", max(results))

k = 3
results = []
for i in range(10000):
    results.append(play(k))
print("Dla ", k, " graczy:")
print("Średnia: ", statistics.mean(results), ". Minimum: ", min(results), ". Maximum: ", max(results))

k = 4
results = []
for i in range(10000):
    results.append(play(k))
print("Dla ", k, " graczy:")
print("Średnia: ", statistics.mean(results), ". Minimum: ", min(results), ". Maximum: ", max(results))

k = 5
results = []
for i in range(10000):
    results.append(play(k))
print("Dla ", k, " graczy:")
print("Średnia: ", statistics.mean(results), ". Minimum: ", min(results), ". Maximum: ", max(results))

k = 6
results = []
for i in range(10000):
    results.append(play(k))
print("Dla ", k, " graczy:")
print("Średnia: ", statistics.mean(results), ". Minimum: ", min(results), ". Maximum: ", max(results))
