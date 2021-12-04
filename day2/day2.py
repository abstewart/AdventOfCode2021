def p1(inp):
    horz = 0
    vert = 0

    for a in inp:
        di = a.split()
        if(di[0] == 'forward'):
            horz += int(di[1])
        elif(di[0] == 'down'):
            vert += int(di[1])
        else:
            vert -= int(di[1])
    
    return [horz,vert]

def p2(inp):
    horz = 0
    vert = 0
    aim = 0
    
    for a in inp:
        di = a.split()
        if(di[0] == 'down'):
            aim += int(di[1])
        elif(di[0] == 'up'):
            aim -= int(di[1])
        else:
            horz += int(di[1])
            vert += (aim*int(di[1]))
    
    return [horz,vert]



if __name__ == '__main__':
    fd = open('input.txt')
    lines = fd.readlines()
    fd.close()

    ret = p1(lines)
    print(ret[0]*ret[1])

    ret = p2(lines)
    print(ret)
    print(ret[0]*ret[1])
