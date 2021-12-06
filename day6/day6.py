

def grow(fishes):
    spawned = 0
    for i, f in enumerate(fishes):
        if f == 0:
            fishes[i] = 6
            spawned += 1
        else:
            fishes[i] = f - 1
    #for i in range(spawned):
        #fishes.append(8)
    fishes.extend([8] * spawned)
    

def simulate(days, fishes):
    for i in range(days):
        print(i)
        grow(fishes)

def printCompFish(fish):
    for i, f in enumerate(fish):
        print('stage:', i, 'fish: ', f)
    print('')

def compress(inp, comp):
    for a in inp:
        comp[a] += 1

def simulateC(days, cfish):
    for i in range(days):
        print(i)
        cfish = growC(cfish)
        #print('cfish:', cfish)
    return cfish

def growC(cfish):
    newcfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, f in enumerate(cfish):
        if i == 0:
            newcfish[6] += f
            newcfish[8] += f
        else:
            newcfish[i-1] += f
    #print(newcfish)
    return newcfish
    

if __name__ == '__main__':
    #format the input
    fd = open('test.txt')
    test_fishes = list(map(int, fd.read().split(',')))
    fd.close

    fd = open('input.txt')
    fishes = list(map(int, fd.read().split(',')))
    fd.close

    #compressed form of the fishes
    cfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    tcfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    #compress(test_fishes, tcfish)
    compress(fishes, cfish)

    #simulate compressed test
    #tcfish = simulateC(256, tcfish)
    #print(tcfish)
    #print(sum(tcfish))

    #simulate compressed actual
    cfish = simulateC(256, cfish)
    print(cfish)
    print(sum(cfish))
    
    
    #print(fishes)
    #simulate(80, test_fishes)
    #print(fishes)
    #print(len(test_fishes))

    #simulate(200, fishes)
    #print(len(fishes))

