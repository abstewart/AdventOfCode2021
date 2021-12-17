
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

def highestPtReached(yvel):
    ans = 0
    while yvel > 0:
        ans += yvel
        yvel -= 1
    return ans

if __name__ == '__main__':
    #format the input
    #target area: x=94..151, y=-156..-103
    tgtx = [94,151]
    tgty = [-156, -103]

    ttgtx = [20,30]
    ttgty = [-10,-5]

    #finding the initial x value
    x = 0
    cnt = 1
    while not (x >= tgtx[0] and x <= tgtx[1]):
        x += cnt
        cnt += 1
    print('part 1 x value: ', cnt)


    yvel = -156
    

    ans = None
    #brute force yvelocities up to 1000
    for i in range(-156, 1000):
        #print('i =', i, 'and ', yHitTarget(i, tgty))
        if yHitTarget(i, tgty):
            ans = i
    print('part 1 y vel: ', ans)
    print('part 1 max y reached ', highestPtReached(ans))
    

    #wrong answers
    #5358 (yvel 102)
        
