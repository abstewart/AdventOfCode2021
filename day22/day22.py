
#converts each line into a tuple
#tup[0] = on or off
#tup[1] = x0, tup[2] = x1
#tup[3] = y1, tup[4] = y2
#tup[5] = z1, tup[6] = z2
def convertInput(lines):
    ans = []
    for a in lines:
        onoff, tmp = a.split(' ')
        x, y, z = tmp.split(',')

        x = x.split('=')[1]
        y = y.split('=')[1]
        z = z.split('=')[1]

        x1, x2 = x.split('..')
        y1, y2 = y.split('..')
        z1, z2 = z.split('..')

        onoff = True if onoff == 'on' else False
        
        ans.append((onoff, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)))
    return ans

def computeReactorStep(reactor, step):
    for i in range(step[1], step[2]+1):
        for j in range(step[3], step[4]+1):
            for k in range(step[5], step[6]+1):
                if step[0]:
                    reactor[(i,j,k)] = 1
                else:
                    if (i,j,k) in reactor:
                        reactor.pop((i,j,k))

if __name__ == '__main__':
    #format the input
    fd = open('test2.txt')
    lines = fd.read().splitlines()
    fd.close


    #print(lines)
    steps = convertInput(lines)
    #dictionary which stores the cubes that have been acted upon
    reactor = {}

    for a in steps:
        computeReactorStep(reactor, a)
    print(len(reactor))



