#
#0 : 6
#1 : 2
#2 : 5
#3 : 5
#4 : 4
#5 : 5
#6 : 6
#7 : 3
#8 : 7
#9 : 6

#solve 1 line of the input, give a list of 10 strings, then a |, then a list of 4 strings
def solveLine(inp):
    alld = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    # in order of the 7-segment display, abcdefg for 01234567
    mapping = ['x', 'x', 'x', 'x', 'x', 'x', 'x']
    unique = [0, 0, 0, 0] #1, 4, 7, 8 in this order
    sixes = list() #0, 6, 9 in some order
    fives = list() #2, 3, 5 in some order

    #split up the input numbers
    for i in range(0, 10):
        b = len(inp[i])
        if b == 2:
            unique[0] = inp[i]
        elif b == 4:
            unique[1] = inp[i]
        elif b == 3:
            unique[2] = inp[i]
        elif b == 7:
            unique[3] = inp[i]
        elif b == 6:
            sixes.append(inp[i])
        else:
            fives.append(inp[i])
    #print(unique)
    #print(sixes)
    #print(fives)

    #mapping[0], what does 7 have that 1 does not?
    tmp = list(unique[2])
    #print(tmp)
    tmp.remove(unique[0][0])
    tmp.remove(unique[0][1])
    #print(tmp)
    mapping[0] = tmp[0]

    #mapping[4]
    #if it contains all of 4, then it's a 9, and we can tell the missing one
    for a in sixes:
        a = set(a)
        four = set(unique[1])
        if four.issubset(a):
            mapping[4] = alld.difference(a).pop()

    #mapping[2] and mapping[5], mapping[1]
    #look for the two in the fives (by looking for mapping[0] and mapping[4]
    for a in fives:
        a = set(a)
        tmp = {mapping[0], mapping[4]}
        if tmp.issubset(a):
            #this is the 2
            tmp = set(list(unique[0]))
            tmp1 = tmp.copy()
            tmp.difference_update(a)
            tmp1.difference_update(tmp)
            mapping[5] = tmp.pop()
            mapping[2] = tmp1.pop()

            #mapping[1] is the (4 - 7) - 2 (using sets)
            #print('unique: ', unique)
            four = set(list(unique[1]))
            seven = set(list(unique[2]))
            #minus the seven
            four.difference_update(seven)
            #minus the 2
            four.difference_update(a)
            mapping[1] = four.pop()
            break

    #mapping[3] is the 4 minus what we know
    tmp = {mapping[1], mapping[2], mapping[5]}
    four = set(list(unique[1]))
    four.difference_update(tmp)
    mapping[3] = four.pop()

    #mapping[6] is what's left
    tmp = {mapping[0], mapping[1], mapping[2], mapping[3], mapping[4], mapping[5]}
    tmp2 = alld.difference(tmp)
    mapping[6] = tmp2.pop()
    #now we know all of the entries        
    #print(mapping)

    #analyze the final 4 numbers
    ans = list()
    for i in range(10, 14):
        c = set(inp[i])
        if c == {mapping[0], mapping[1], mapping[2], mapping[4], mapping[5], mapping[6]}:
            ans.append('0')
        elif len(c) == 2:
            ans.append('1')
        elif c == {mapping[0], mapping[2], mapping[3], mapping[4], mapping[6]}:
            ans.append('2')
        elif c == {mapping[0], mapping[2], mapping[3], mapping[5], mapping[6]}:
            ans.append('3')
        elif len(c) == 4:
            ans.append('4')
        elif c == {mapping[0], mapping[1], mapping[3], mapping[5], mapping[6]}:
            ans.append('5')
        elif c == {mapping[0], mapping[1], mapping[3], mapping[4], mapping[5], mapping[6]}:
            ans.append('6')
        elif len(c) == 3:
            ans.append('7')
        elif len(c) == 7:
            ans.append('8')
        else:
            ans.append('9')
    #print(ans)
    #print(int("".join(ans)))   
    #print('value of line: ', int(str(ans)))
    return (int("".join(ans)))
            
def oldCode():
    #first work out the easy ones:
    for a in inp:
        #decode the 1, 7, 4 (8 is useless i think)
        for i in range(10, 14):
            b = len(a[i])
            if b == 2:
                #this is a 1
                mapping[2] = a[i][0]
                mapping[5] = a[i][1]
            if b == 3:
                #this is a 7, only care about the top
                mapping[0] = a[i][0]
            if b == 4:
                #this is a 4
                mapping[1] = a[i][0]
                mapping[3] = a[i][2]

        for i in range(10, 14):
            b = len(a[i])


if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    inputs = fd.readlines()
    fd.close

    fd = open('test.txt')
    tin = fd.readlines()
    fd.close


    #format the input
    #strip the newlines
    inputs = list(map(lambda s: s.strip(), inputs))
    tin = list(map(lambda s: s.strip(), tin))

    #format each line
    for i, a in enumerate(inputs):
        inputs[i] = a.split(' ')
        inputs[i].remove('|')
    for i, a in enumerate(tin):
        tin[i] = a.split(' ')
        tin[i].remove('|')

    #single line testing
    sl = ['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab', 'cdfeb', 'fcadb', 'cdfeb', 'cdbaf']
    #printing
    #print(tin)
    
    #each entry is now a list of 10 strings, a '|' and 4 more strings

    #part1
    cnt = 0
    for a in tin:
        for i in range(10, 14):
            b = len(a[i])
            if b == 2 or b == 3 or b == 4 or b == 7:
                cnt += 1
    print('part 1 test input ans: ', cnt)

    cnt = 0
    for a in inputs:
        for i in range(10, 14):
            b = len(a[i])
            if b == 2 or b == 3 or b == 4 or b == 7:
                cnt += 1
    print('part 1 actual ans: ', cnt)

    #part2
    #testing for part 2
    print("test line conversion: ", solveLine(sl))

    ans = 0
    for i in tin:
        #print(i)
        tmp = solveLine(i)
        #print(tmp)
        ans += tmp
    print('part2 testing answer: ', ans)

    ans = 0
    for i in inputs:
        ans += solveLine(i)
    print('part2 actual answer: ', ans)
