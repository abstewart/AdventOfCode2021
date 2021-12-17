
def yHitTarget(yvel, tgty):
    ypos = 0
    while True:
        #print(ypos)
        if ypos < tgty[0]:
            return False
        if ypos >= tgty[0] and ypos <= tgty[1]:
            return True
        ypos += yvel
        yvel -= 1

def hitTarget(xvel, yvel, tgtx, tgty):
    xpos = 0
    ypos = 0
    while True:
        xpos += xvel
        xvel -= 1 if xvel > 0 else 0
        ypos += yvel
        yvel -= 1
        if ypos < tgty[0] or xpos > tgtx[1]:
            return False
        if (ypos >= tgty[0] and ypos <= tgty[1]) and (xpos >= tgtx[0] and xpos <= tgtx[1]):
            return True

if __name__ == '__main__':
    #format the input
    #target area: x=94..151, y=-156..-103
    tgtx = [94,151]
    tgty = [-156, -103]

    ttgtx = [20,30]
    ttgty = [-10,-5]



    ans = set()
    for i in range(300):
        for j in range(-200, 300):
            if hitTarget(i, j, tgtx, tgty):
                ans.add((i,j))
    print(len(ans))

    

    #wrong answers
    #5358 (yvel 102)
        
