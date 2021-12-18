import math

def printlines(lines):
    for a in lines:
        print(a)
    return

def printline(line):
    ans = ''
    for i, a in enumerate(line):
        ans += str(a)
        if a == ']' or (isinstance(a, int) and isinstance(line[i+1], int)):
            ans += ', '
    print(ans)
    return ans

def formatline(strline):
    ans = []
    for a in strline:
        if a == ',':
            continue
        elif a == '[' or a == ']':
            ans.append(a)
        else:
            #it's a digit, and regular inputs are never >= 10
            ans.append(int(a))
    return ans

def explodeline(i1, i2, line):
    x = line[i1] #left val
    y = line[i2] #right val

    #search the left side of the list to add x to
    j = i1-2
    while j >= 0:
        if isinstance(line[j], int):
            line[j] += x
            break
        j -= 1

    #search the right side of the list to add y to
    j = i2+1
    while j < len(line):
        if isinstance(line[j], int):
            line[j] += y
            break
        j += 1

    #remove the exploded element and add a 0
    for k in range(4):
        del line[i1-1]
    line.insert(i1-1, 0)
    #return
    return line

#returns whether or not an explosion happened
def findExplosion(line):
    deep = 0
    for i, a in enumerate(line):
        if a == '[':
            deep += 1
            continue
        elif a == ']':
            deep -= 1
            continue
        #if deep is >= 5 and current entry is a number and next in list is a number, found an explosion
        #if we're currently on a number, there will always be another element in the list
        if deep > 4 and isinstance(a, int) and isinstance(line[i+1], int):
            explodeline(i, i+1, line)
            return True
    return False
    
    
def findSplit(line):
    for i, a in enumerate(line):
        if isinstance(a, int) and a >= 10:
            x = math.floor(a/2)
            y = math.ceil(a/2)
            #remove the old number
            del line[i]
            line.insert(i, '[')
            line.insert(i+1, x)
            line.insert(i+2, y)
            line.insert(i+3, ']')
            return True
    return False

def findResult(line):
    #loop through the line, first exploding, the possibly splitting
    while True:
        while True:
            if not findExplosion(line):
                break
        if not findSplit(line):
            break
    return line

def add2lines(l1, l2):
    #add the two lists, with enclosing brackets
    ans = []
    ans.append('[')
    ans = ans + l1
    ans = ans + l2
    ans.append(']')
    return ans

def combineAllLines(lines):
    tmp = lines.pop(0)
    ans = formatline(tmp)

    #while there are more lines in the input
    for a in lines:
        tmp = formatline(a)
        tmp1 = add2lines(ans, tmp)
        ans = findResult(tmp1)
        printline(ans)

    return ans

def findMagnitude(line):
    ll = line.copy()
    while len(ll) > 4:
        #still more magnitude calculating to be found
        for i, a in enumerate(ll):
            if isinstance(a, int) and isinstance(ll[i+1], int):
                ll[i] = ll[i]*3 + ll[i+1]*2
                del ll[i-1]
                del ll[i]
                del ll[i]
                break
    return ll[1]*3 + ll[2]*2

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    lines = fd.read().splitlines()
    fd.close

    curr = []
    l1 = formatline(lines[0])
    l2 = formatline(lines[1])

    ls = add2lines(l1, l2)

    lis = lines.copy()

    
    #print(l1)
    #print(l2)
    #print(ls)
    #print('trying to find result')
    #findResult(ls)
    #printline(ls)

    #part 1
    #print('combining all lines')
    #ans = combineAllLines(lis)
    #printline(ans)
    #print('part 1 ans: ', findMagnitude(ans))

    #part 2
    ans = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                l1 = formatline(lines[i])
                l2 = formatline(lines[j])
                tmp = add2lines(l1, l2)
                findResult(tmp)
                ans.append(findMagnitude(tmp))
    print('part 2 ans: ', max(ans))

    
