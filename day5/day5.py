def printventmap(vmap):
    for a in vmap:
        print(a)
    print('')

def convertToPoints(raw_points):
    for i, a in enumerate(raw_points):
        tmp = raw_points[i]
        tmp = tmp.split(' -> ')
        for j, b in enumerate(tmp):
            b = tuple(map(int, b.split(',')))
            tmp[j] = b
        raw_points[i] = tmp
    return raw_points

def fillVentMap(points, vmap, pt2):
    #loop through all the inputs
    for a in points:
        x1 = a[0][0]
        x2 = a[1][0]
        y1 = a[0][1]
        y2 = a[1][1]
        #print(a)
        #are the x's the same?
        if(x1 == x2):
            #do stuff depending on the order of the 2 y values
            if(y1 < y2):
                for i in range(y1, y2 + 1):
                    vmap[i][x1] += 1
            else:#y2 < y1
                for i in range(y2, y1 + 1):
                    vmap[i][x1] += 1
        elif(y1 == y2):
            #add the points to the map depending on the order of the 2 x values
            if(x1 < x2):
                for i in range(x1, x2 + 1):
                    vmap[y1][i] += 1
            else:#x2 < x1
                for i in range(x2, x1 + 1):
                    vmap[y1][i] += 1
        elif(pt2):
            if x1 < x2 and y1 < y2:
                for i, j in zip(range(x1,x2+1), range(y1,y2+1)):
                    vmap[j][i] += 1
            elif x1 < x2 and y2 < y1:
                for i, j in zip(range(x1,x2+1), range(y1,y2-1,-1)):
                    vmap[j][i] += 1
            elif x2 < x1 and y1 < y2:
                for i, j in zip(range(x1,x2-1,-1), range(y1,y2+1)):
                    vmap[j][i] += 1
            elif x2 < x1 and y2 < y1:
                for i, j in zip(range(x1,x2-1,-1), range(y1,y2-1,-1)):
                    vmap[j][i] += 1
                
        #printventmap(vmap)
    return vmap

def findDanger(vmap):
    cnt = 0
    for a in vmap:
        for b in a:
            if b >= 2:
                cnt += 1
    return cnt

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    my_points = fd.read().splitlines()
    fd.close
    fd = open('test.txt')
    test_points = fd.read().splitlines()
    fd.close
    
    convertToPoints(my_points)
    #print(my_points)
    convertToPoints(test_points)
    #print(test_points)

    #format the 2D list ventmap
    smallventmap = [0] * 10
    for i in range(len(smallventmap)):
        smallventmap[i] = [0] * 10
    #printventmap(smallventmap)
    ventmap = [0] * 1000
    for i in range(len(ventmap)):
        ventmap[i] = [0]*1000
    #print(ventmap[999][999])

    #fill the ventmap with the vents for part 1
    #fillVentMap(my_points, ventmap, False)
    #fillVentMap(test_points, smallventmap, False)
    #printventmap(smallventmap)

    #fill the ventmap with the vents for part 2
    fillVentMap(my_points, ventmap, True)
    #fillVentMap(test_points, smallventmap, True)

    #Find number of hot vents
    #print(findDanger(smallventmap))
    #print('part1 hotspots: ', findDanger(ventmap))
    print('part2 hostspots:', findDanger(ventmap))
    #print the maps if desired
    #printventmap(smallventmap)
    #printventmap(ventmap)


def testing_code():
    test = '10,50 -> 10,55'
    print(test)
    test = test.split(' -> ')
    print(test)
    for i, b in enumerate(test):
        b = tuple(b.split(','))
        test[i] = b
    print(test)
    print(type(test))
    print(type(test[0]))
    print(test[0][0])
    
