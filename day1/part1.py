def p1(inp):
    count = 0
    prev = 0
    for d in inp:
        #print(d)
        #print(prev)
        #print(d-prev)
        if (d-prev) > 0:
            count += 1
        prev = d
    count -= 1
    print(count)

if __name__ == '__main__' :
    fd = open('input.txt')
    lines = fd.readlines()
    fd.close()
    lines = list(map(int, lines))

    p1(lines)
    
    i = 0
    llines = list()
#    print(lines[1])
#    llines.append(lines[0]+lines[1]+lines[2])
    while i < len(lines)-2:
        llines.append(lines[i] + lines[i+1] + lines[i+2])
        i += 1

    p1(llines)
