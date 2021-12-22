#import math
#converts each line into a tuple
#tup[0] = on or off
#tup[1] = x0, tup[2] = x1
#tup[3] = y1, tup[4] = y2
#tup[5] = z1, tup[6] = z2

class Region():
    def __init__(self, on, x1, x2, y1, y2, z1, z2):
        self.on = on
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.adj = [] #list of regions that adjust this one, may be deep

    def countCubes(self):
        ans = 0
        x = abs(self.x2-self.x1) + 1
        y = abs(self.y2-self.y1) + 1
        z = abs(self.z2-self.z1) + 1
        print(x,y,z)
        if self.on:
            ans =  x * y * z
        else:
            ans =  -1 * x * y * z
        print(type(ans))
        print(ans)
        return ans

    def area(self):
        ans = countCubes2(self)
        for a in self.adj:
            tmp = a.area()
            ans += tmp
        return ans
    
def countCubes2(cube):
    ans = 0
    x = abs(cube.x2-cube.x1) + 1
    y = abs(cube.y2-cube.y1) + 1
    z = abs(cube.z2-cube.z1) + 1
    #print(x,y,z)
    if cube.on:
        ans =  x * y * z
    else:
        ans =  -1 * x * y * z
    #print(type(ans))
    #print(ans)
    return ans
    

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
        
        #ans.append((onoff, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)))
        tmp = Region(onoff, int(x1), int(x2), int(y1), int(y2), int(z1), int(z2))
        ans.append(tmp)
    return ans

#returns true if the two regions intersect one another, false otherwise
def intersect(r1, r2):
    return not (r1.x1 > r2.x2 or r1.x2 < r2.x1 or
                r1.y1 > r2.y2 or r1.y2 < r2.y1 or
                r1.z1 > r2.z2 or r1.z2 < r2.z1)


def findDirectIntersection(r1, r2):
    if not intersect(r1, r2):
        return None
    x1 = max(r1.x1, r2.x1)
    x2 = min(r1.x2, r2.x2)
    y1 = max(r1.y1, r2.y1)
    y2 = min(r1.y2, r2.y2)
    z1 = max(r1.z1, r2.z1)
    z2 = min(r1.z2, r2.z2)
    if r1.on and r2.on:
        on = False
    elif r1.on and not r2.on:
        on = False
    elif not r1.on and r2.on:
        on = True
    elif not r1.on and not r2.on:
        on = True
    return Region(on,x1,x2,y1,y2,z1,z2)

#adjusts the regions in the list with r2
#r2 should initially be an 'off' region
def adjustRegionList(r1s, r2):
    ans = []
    for a in r1s:
        ans.append(adjustRegion1(a, r2))
    return ans

#adds adjustment to the first region
#returns the adjusted region?
def adjustRegion1(r1, r2):
    tmp = findDirectIntersection(r1, r2)
    #check if the regions don't overlap
    if not tmp:
        return r1 #don't adjust the region at all
    r1.adj = adjustRegionList(r1.adj, tmp)
    r1.adj.append(tmp)
    return r1

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    lines = fd.read().splitlines()
    fd.close


    #print(lines)
    steps = convertInput(lines)
    #dictionary which stores list of regions
    reactor = []
    #for a in steps:
    #print('loop countCubes: ', countCubes2(a))
    #print('loop countArea: ', a.area())

    #loop through the steps
    s = 0
    for a in steps:
        print('step: ', s)
        s += 1
        #update the reactor with this new region
        for i, b in enumerate(reactor):
            reactor[i] = adjustRegion1(b, a)
        if a.on:
            reactor.append(a)

    ans = 0
    for a in reactor:
        tmp = a.area()
        ans += tmp
    print('ans equals: ', ans)
