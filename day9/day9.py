
def findLowPoints(arr):
    ans = 0
    #find the low points
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            lowpt = True
            a = arr[i][j]
            #print(i, j)
            if i == 0:
                if arr[i+1][j] <= a:
                    lowpt = False
            elif i == len(arr) - 1:
                if arr[i-1][j] <= a:
                    lowpt = False
            else:
                if arr[i-1][j] <= a or arr[i+1][j] <= a:
                    lowpt = False
            if j == 0:
                if arr[i][j+1] <= a:
                    lowpt = False
            elif j == len(arr[i]) - 1:
                if arr[i][j-1] <= a:
                    lowpt = False
            else:
                if arr[i][j-1] <= a or arr[i][j+1] <= a:
                    lowpt = False
            #if the point is still a lowpt, add 1+value to the ans
            if(lowpt):
                ans += arr[i][j]+1
    return ans

#returns a list of the low point indixes in a list
def findLowPointsList(arr):    
    ans = list()
    #find the low points
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            lowpt = True
            a = arr[i][j]
            #print(i, j)
            if i == 0:
                if arr[i+1][j] <= a:
                    lowpt = False
            elif i == len(arr) - 1:
                if arr[i-1][j] <= a:
                    lowpt = False
            else:
                if arr[i-1][j] <= a or arr[i+1][j] <= a:
                    lowpt = False
            if j == 0:
                if arr[i][j+1] <= a:
                    lowpt = False
            elif j == len(arr[i]) - 1:
                if arr[i][j-1] <= a:
                    lowpt = False
            else:
                if arr[i][j-1] <= a or arr[i][j+1] <= a:
                    lowpt = False
            #if the point is still a lowpt, add 1+value to the ans
            if(lowpt):
                ans.append([i,j])
    return ans

#recursive function to find the size of a basin
#arr is the entire arr to search
#tosearch is a list of points which might be part of the basin
#i is the place in tosearch which we are currently checking
#returns a list of the points in the basin
def findSizeOfBasin(arr, tosearch, ind):
    #is this point a 9?
    i = tosearch[ind][0]
    j = tosearch[ind][1]
    if arr[i][j] == 9:
        #keep looking without adding anything
        return findSizeOfBasin(arr, tosearch, i+1)
    #add upto the four surrounding points to the tosearch list, if they exist and arent already in there
    if i == 0:
        if [i+1,j] not in arr: tosearch.append([i+1,j])
    elif i == len(arr) - 1:
        if [i-1,j] not in arr: tosearch.append([i-1,j])
    else:
        if [i+1,j] not in arr: tosearch.append([i+1,j])
        if [i-1,j] not in arr: tosearch.append([i-1,j])
    if j == 0:
        if [i,j+1] not in arr: tosearch.append([i,j+1])
    elif j == len(arr[i]) - 1:
        if [i,j-1] not in arr: tosearch.append([i,j-1])
    else:
        if [i,j+1] not in arr: tosearch.append([i,j+1])
        if [i,j-1] not in arr: tosearch.append([i,j-1])
    #recurse on the next element in the list and add this one to the ans

    #are we done searching?
    if ind == len(tosearch) - 1:
        return list() #bottom of the function, now append all the valid basin pts into this list
    else:
        return findSizeOfBasin(arr, tosearch, ind+1).append([i,j])

def findSizeOfBasin2(arr, tosearch):
    ans = list()
    for a in tosearch:
        #print(a)
        #print(tosearch)
        if (len(tosearch) > 500):
            break
        i = a[0]
        j = a[1]
        if arr[i][j] == 9:
            continue
        if [i,j] not in ans:
            ans.append([i,j])
        if i == 0:
            if [i+1,j] not in tosearch:
                tosearch.append([i+1,j])
        elif i == len(arr) - 1:
            if [i-1,j] not in tosearch:
                tosearch.append([i-1,j])
        else:
            if [i+1,j] not in tosearch:
                tosearch.append([i+1,j])
            if [i-1,j] not in tosearch:
                tosearch.append([i-1,j])
        if j == 0:
            if [i,j+1] not in tosearch:
                tosearch.append([i,j+1])
        elif j == len(arr[i]) - 1:
            if [i,j-1] not in tosearch:
                tosearch.append([i,j-1])
        else:
            if [i,j+1] not in tosearch:
                tosearch.append([i,j+1])
            if [i,j-1] not in tosearch:
                tosearch.append([i,j-1])
    return ans
def findAllBasins(arr):
    basins = list()
    #find all the low points in the arr
    lp = findLowPointsList(arr)
    #print(lp)
    #find all the basins with each lp as the starting one (may be some overlap)
    for a in lp:
        basins.append(findSizeOfBasin2(arr, [a]))
    #now get rid of duplicate basins #TODO
    for i, a in enumerate(basins):
        j = i+1
        #print('i: ', i, 'a: ', a)
        while j < len(basins):
            #print(j)
            if a[0] in basins[j]:
                del basins[j]
                j -= 1
            j += 1
    #now convert to numbers to return
    ans = list(map(len, basins))
    return ans

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    inputs = fd.readlines()
    fd.close

    fd = open('test.txt')
    tin = fd.readlines()
    fd.close

    #format inputs
    for i in range(len(tin)):
        tin[i] = list(map(int, list(tin[i].strip())))
    for i in range(len(inputs)):
        inputs[i] = list(map(int, list(inputs[i].strip())))
    
    print(tin)
    #for a in inputs:
    #print(a)

    print('pt 1 testing ans: ', findLowPoints(tin))
    print('pt 1 actual ans: ', findLowPoints(inputs))
    #not 1910!

    pt2test = findAllBasins(tin)
    while len(pt2test) > 3:
        pt2test.remove(min(pt2test))
    print('pt 2 testing ans: ', pt2test[0] * pt2test[1] * pt2test[2])
    pt2act = findAllBasins(inputs)
    while len(pt2act) > 3:
        pt2act.remove(min(pt2act))
    print('pt 2 actual ans: ', pt2act[0] * pt2act[1] * pt2act[2])
    
                    
