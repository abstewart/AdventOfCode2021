def fuel_required(f, crabs):
    ans = 0
    for i in crabs:
        if f > i:
            ans += (f-i)
        else:
            ans += (i-f)
    return ans

def find_fuel_cost(x1, x2):
    ans = 0
    if x1 < x2:
        for i, x in enumerate(range(x1, x2)):
            ans += i+1
    else:
        for i, x in enumerate(range(x2, x1)):
            ans += i+1
    return ans

def fuel_required2(f, crabs):
    ans = 0
    for i in crabs:
        ans += find_fuel_cost(i, f)
    return ans


def find_best_value(crabs):
    ans = fuel_required(0, crabs)
    for i in range(1, max(crabs)):
        tmp = fuel_required(i, crabs)
        if tmp < ans:
            ans = tmp
    return ans

def find_best_value2(crabs):
    ans = fuel_required2(0, crabs)
    for i in range(1, max(crabs)):
        print(i)
        tmp = fuel_required2(i, crabs)
        if tmp < ans:
            ans = tmp
    return ans

if __name__ == '__main__':
    #format the input
    fd = open('test.txt')
    test_crabs = list(map(int, fd.read().split(',')))
    fd.close

    fd = open('input.txt')
    crabs = list(map(int, fd.read().split(',')))
    fd.close

    
    print(test_crabs)
    print(sum(test_crabs) / len(test_crabs))
    #print(fuel_required(2, test_crabs))
    print('test pt1: ', find_best_value(test_crabs))
    print('test pt2: ', find_best_value2(test_crabs))

    print(max(crabs))
    #print('pt 1: least fuel required: ', find_best_value(crabs))
    print('pt 2: least fuel required: ', find_best_value2(crabs))
    #testing
    #for i, j in enumerate(range(6, 9)):
        #print(i, j)
