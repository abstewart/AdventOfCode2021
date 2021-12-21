
class deterministicDie():
    def __init__(self):
        self.prev_roll = 0
        self.rolls = 0
    def roll(self):
        self.prev_roll += 1
        if self.prev_roll > 100:
            self.prev_roll = 1
        self.rolls += 1
        return self.prev_roll

def unfinishedGame(dic):
    for a in dic.keys():
        if dic[a] != 0:
            print(a)
            return True
    return False
#returns an updated state depending on the die roll and if it's p1's turn
def updateState(state, p1turn, dieroll):
    p1pos = state[0] 
    p2pos = state[1] 
    p1score = state[2]
    p2score = state[3]

    if p1turn:
        p1pos += dieroll
        if p1pos > 10:
            p1pos -= 10
        p1score += p1pos
        return (p1pos, p2pos, p1score, p2score)
    else: #p2's turn
        p2pos += dieroll
        if p2pos > 10:
            p2pos -= 10
        p2score += p2pos
        return (p1pos, p2pos, p1score, p2score)

#games is the dictionary of game states
#p1turn is true if it is p1's turn, false if it is p2's turn
def simulateQuantumTurn(games, p1turn, blank_dict):
    ans = blank_dict.copy()
    win = 0
    for state, count in games.items():
    
        if p1turn:
            #27 possible outcomes
            #1 situation where dierolls = 3 (1,1,1)x1
            tmp = updateState(state, True, 3)
            if(tmp[2] >= 21):
                win += count
            else:
                ans[tmp] += count
            #3 situations where dierolls = 4 (1,1,2)x3
            tmp = updateState(state, True, 4)
            if(tmp[2] >= 21):
                win += count * 3
            else:
                ans[tmp] += count * 3
            #6 situations where dierolls = 5 (1,1,3)x3, (1,2,2)x3
            tmp = updateState(state, True, 5)
            if(tmp[2] >= 21):
                win += count * 6
            else:
                ans[tmp] += count * 6
            #7 situations where dierolls = 6 (1,2,3)x6, (2,2,2)x1
            tmp = updateState(state, True, 6)
            if(tmp[2] >= 21):
                win += count * 7
            else:
                ans[tmp] += count * 7
            #6 situations where dierolls = 7 (2,2,3)x3, (1,3,3)x3
            tmp = updateState(state, True, 7)
            if(tmp[2] >= 21):
                win += count * 6
            else:
                ans[tmp] += count * 6
            #3 situations where dierolls = 8 (2,3,3)x3
            tmp = updateState(state, True, 8)
            if(tmp[2] >= 21):
                win += count * 3
            else:
                ans[tmp] += count * 3
            #1 situation where dierolls = 9 (3,3,3)x1
            tmp = updateState(state, True, 9)
            if(tmp[2] >= 21):
                win += count
            else:
                ans[tmp] += count
        else:
            #27 possible outcomes in 9 groups
            #1 situation where dierolls = 3 (1,1,1)x1
            tmp = updateState(state, False, 3)
            if(tmp[3] >= 21):
                win += count
            else:
                ans[tmp] += count
            #3 situations where dierolls = 4 (1,1,2)x3
            tmp = updateState(state, False, 4)
            if(tmp[3] >= 21):
                win += count * 3
            else:
                ans[tmp] += count * 3
            #6 situations where dierolls = 5 (1,1,3)x3, (1,2,2)x3
            tmp = updateState(state, False, 5)
            if(tmp[3] >= 21):
                win += count * 6
            else:
                ans[tmp] += count * 6
            #7 situations where dierolls = 6 (1,2,3)x6, (2,2,2)x1
            tmp = updateState(state, False, 6)
            if(tmp[3] >= 21):
                win += count * 7
            else:
                ans[tmp] += count * 7
            #6 situations where dierolls = 7 (2,2,3)x3, (1,3,3)x3
            tmp = updateState(state, False, 7)
            if(tmp[3] >= 21):
                win += count * 6
            else:
                ans[tmp] += count * 6
            #3 situations where dierolls = 8 (2,3,3)x3
            tmp = updateState(state, False, 8)
            if(tmp[3] >= 21):
                win += count * 3
            else:
                ans[tmp] += count * 3
            #1 situation where dierolls = 9 (3,3,3)x1
            tmp = updateState(state, False, 9)
            if(tmp[3] >= 21):
                win += count
            else:
                ans[tmp] += count
    #loop through the game dict and update with answers
    return ans, win
if __name__ == '__main__':

    #make the blank uniDict
    blank_uniDict = {}
    #there are 10 spots p1 can be
    for i in range(1, 11):
        #there are 10 spots p2 can be
        for j in range(1, 11):
            #there are 0-20 = 21 different scores possible for p1 (anything larger and someonw has won)
            for k in range(21):
                #there are 0-20 = 21 different scores possible for p2 (anything larger and someone has won)
                for l in range(21):
                    blank_uniDict[(i,j,k,l)] = 0
    print(len(blank_uniDict))
                    
        
    
    
    #actual starting pts
    p1pos = 5
    p2pos = 9
    #testing starting pts
    #p1pos = 4
    #p2pos = 8
    p1turn = True #p1 starts first
    p1wins = 0
    p2wins = 0
    gameDict = blank_uniDict.copy()
    gameDict[(p1pos,p2pos,0,0)] = 1
    cnt = 0
    print(gameDict[(4,8,0,0)])
    print(blank_uniDict[(4,8,0,0)])
    print(unfinishedGame(gameDict))
    print('starting quantum game')
    while unfinishedGame(gameDict):
        if p1turn:
            gameDict, cnt = simulateQuantumTurn(gameDict, p1turn, blank_uniDict)
            p1wins += cnt
            p1turn = False
        else:
            gameDict, cnt = simulateQuantumTurn(gameDict, p1turn, blank_uniDict)
            p2wins += cnt
            p1turn = True
    print('p1 wins: ', p1wins)
    print('p2 wins: ', p2wins)
    #the quantum game
    #add the initial states to the game

    #ans:
    #430229563871565
    
    #not the right ans:
    #444356092776315
    #444356092776315
