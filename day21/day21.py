
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
        

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    lines = fd.read().splitlines()
    fd.close

    #actual starting pts
    p1pos = 5
    p2pos = 9
    #testing starting pts
    #p1pos = 4
    #p2pos = 8
    p1score = 0
    p2score = 0
    p1turn = True #p1 starts first
    gameDie = deterministicDie()

    #playing the game
    while p1score < 1000 and p2score < 1000:
        if p1turn:
            p1pos += (gameDie.roll() + gameDie.roll() + gameDie.roll())
            while p1pos > 10:
                p1pos -= 10
            p1score += p1pos
            p1turn = False
            #print('p1pos: ', p1pos, 'p1score: ', p1score, 'dice prev_roll', gameDie.prev_roll)
        else:
            p2pos += (gameDie.roll() + gameDie.roll() + gameDie.roll())
            while p2pos > 10:
                p2pos -= 10
            p2score += p2pos
            p1turn = True
            #print('p2pos: ', p2pos, 'p2score: ', p2score, 'dice prev_roll', gameDie.prev_roll)
            

    lowerScore = p2score if p1score >= 1000 else p1score
    numRolls = gameDie.rolls
    print('lowerScore: ', lowerScore)
    print('numrolls: ', numRolls)
    print('score*rolls: ', lowerScore*numRolls)
    
            
