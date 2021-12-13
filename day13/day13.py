
#actually look at the x values...
def foldY(pts, val):
    ans = set()
    print('folding along y =', val)
    for a in pts:
        if a[1] > val:
            togo = a[1] - val
            if val - togo >=0:
                ans.add((a[0], val-togo))
        else:
            ans.add(a)
    #print('ret', ans)
    return ans

#actually look at the y values...
def foldX(pts, val):
    ans = set()
    print('folding along x =', val)
    for a in pts:
        if a[0] > val:
            togo = a[0] - val
            if val-togo >= 0:
                ans.add((val-togo, a[1]))
        else:
            ans.add(a)
    return ans

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    inputs = fd.read().splitlines()
    fd.close

    fd = open('test.txt')
    tst = fd.read().splitlines()
    fd.close

    tstDir = []
    inpDir = []
    #format inputs
    tstDir.insert(0, tst.pop())
    tstDir.insert(0, tst.pop())
    tst.pop()
    for i, a in enumerate(tst):
        tst[i] =  tuple(map(int, a.split(',')))
    #print(type(tst))
    tst = set(tst)
    for i in range(12):
        inpDir.insert(0, inputs.pop())
    inputs.pop()
    for i, a in enumerate(inputs):
        inputs[i] = tuple(map(int, a.split(',')))
    inputs = set(inputs)


    #make the paper arr
    
    
    print(tst)
    print(tstDir)
    quit
    #do the folding
    tstans = tst
    for a in tstDir:
        if 'y' in a:
            tstans = foldY(tstans, int(a[13:]))
            print('len: ', len(tstans))
        elif 'x' in a:
            tstans = foldX(tstans, int(a[13:]))
    #print(tstans)

    actans = inputs
    #actans = foldX(actans, 655)
    #print('actans len: ', len(actans))
    for a in inpDir:
        if 'y' in a:
            actans = foldY(actans, int(a[13:]))
        elif 'x' in a:
            actans = foldX(actans, int(a[13:]))
    #print(actans)

    prin = ['.'] * 50
    for i in range(len(prin)):
        prin[i] = ['.'] * 50
    for a in actans:
        x = a[1]
        y = a[0]
        prin[x][y] = '#'
    #print(prin)
    for a in prin:
        print(a)
    #testing
