def printOcto(arr):
    for a in arr:
        print(a)
    return

def updateSurrounding(x, y, arr):
    #x,y are the coordinates of the exploding octopus
    #top of the arr
    if x == 0:
        #left side of the arr
        if y == 0:
            arr[x+1][y][0]   += 1
            arr[x][y+1][0]   += 1
            arr[x+1][y+1][0] += 1
        #right side of the arr
        elif y == 9:
            arr[x+1][y][0]   += 1
            arr[x][y-1][0]   += 1
            arr[x+1][y-1][0] += 1
        #middle of the arr
        else:
            arr[x][y+1][0]   += 1
            arr[x][y-1][0]   += 1
            arr[x+1][y-1][0] += 1
            arr[x+1][y][0]   += 1
            arr[x+1][y+1][0] += 1
    #bottom of the arr
    elif x == 9:
        #left side of the arr
        if y == 0:
            arr[x-1][y][0]   += 1
            arr[x][y+1][0]   += 1
            arr[x-1][y+1][0] += 1
        #right side of the arr
        elif y == 9:
            arr[x-1][y][0]   += 1
            arr[x][y-1][0]   += 1
            arr[x-1][y-1][0] += 1
        #middle of the arr
        else:
            arr[x][y+1][0]   += 1
            arr[x][y-1][0]   += 1
            arr[x-1][y-1][0] += 1
            arr[x-1][y][0]   += 1
            arr[x-1][y+1][0] += 1
    #middle of the arr
    else:
        #lef side of the arr
        if y == 0:
            arr[x-1][y][0]   += 1
            arr[x+1][y][0]   += 1
            arr[x-1][y+1][0] += 1
            arr[x][y+1][0]   += 1
            arr[x+1][y+1][0] += 1
        #right side of the arr
        elif y == 9:
            arr[x-1][y][0]   += 1
            arr[x+1][y][0]   += 1
            arr[x-1][y-1][0] += 1
            arr[x][y-1][0]   += 1
            arr[x+1][y-1][0] += 1
        #true middle of the arr
        else:
            arr[x-1][y-1][0] += 1
            arr[x-1][y][0]   += 1
            arr[x-1][y+1][0] += 1
            arr[x][y-1][0]   += 1
            arr[x][y+1][0]   += 1
            arr[x+1][y-1][0] += 1
            arr[x+1][y][0]   += 1
            arr[x+1][y+1][0] += 1
        
    return

def explode(arr):
    ans = 0
    for i, a in enumerate(arr):
        for j, b in enumerate(a):
            if b[0] > 9 and not b[1]:
                b[1] = True #it has exploded
                ans += 1
                updateSurrounding(i, j, arr)
    return ans

def unexploded(arr):
    #are there any unexploded fish in the arr?
    ans = False
    for a in arr:
        for b in a:
            #print(b[0])
            if b[0] > 9 and not b[1]:
                return True
    return ans

def incBrightness(arr):
    for a in arr:
        for b in a:
            b[0] += 1
    return

def resetExploded(arr):
    for a in arr:
        for b in a:
            if b[1]:
                b[0] = 0
                b[1] = False
    return

def simulateDay(arr):
    explosions = 0
    #go through the arr, if there are any un-exploded with value > 9, explode them
    #then do it again while unexploded
    #STEP 1: increase the energy level of each octopus
    incBrightness(arr)

    #STEP 2: chain exploding
    while unexploded(arr):
        explosions += explode(arr)
        
    #STEP 3: reset exploded octopus
    resetExploded(arr)
    return explosions

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    inputs = fd.readlines()
    fd.close

    fd = open('test.txt')
    tst = fd.readlines()
    fd.close

    #format inputs
    for i, a in enumerate(tst):
        li = []
        a = a.strip()
        for b in a:
            li.append([int(b), False])
        tst[i] = li

    for i, a in enumerate(inputs):
        li = []
        a = a.strip()
        for b in a:
            li.append([int(b), False])
        inputs[i] = li



    #ans = 0
    #for i in range(100):
        #ans += simulateDay(tst)
    #print('pt 1 testing ans: ', ans)

    #ans = 0
    #for i in range(100):
        #ans += simulateDay(inputs)
    #print('pt 1 actual ans: ', ans)

    cont = True
    cnt = 0
    while cont:
        cnt += 1
        if simulateDay(inputs) == 100:
            cont = False
    print(cnt)
    #printing stuff
    #printOcto(tst)
    #print('first day')
    #print(simulateDay(tst))
    #printOcto(tst)
    #print('2nd day')
    #print(simulateDay(tst))
    #printOcto(tst)




