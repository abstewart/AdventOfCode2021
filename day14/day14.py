from collections import Counter

def convertSubs(sublist):
    ans = dict()
    for a in sublist:
        tmp = tuple(a.split(' -> '))
        ans.update({tmp[0] : tmp[1]})
    return ans

def subst(poly, subdict):
    i = 0
    j = 2
    newpoly = poly
    while j < len(newpoly)+1:
        key = newpoly[i:j]
        val = subdict.get(key)
        if val:
            tmppoly = newpoly[0:i+1] + val + newpoly[i+1:]
            newpoly = tmppoly
            #move the sliding window by 1 to not consider the newly added char
            i += 1
            j += 1
        i += 1
        j += 1
    return newpoly

def subst2(polydict, subdict, blankpolydict):
    newdict = blankpolydict.copy()
    for a in polydict.keys():
        #if this pair of chars exists in the polydict, and it has a insertable from subdict
        if polydict[a] > 0 and subdict.get(a):
            cnts = polydict[a]
            key1 = a[0:1] + subdict.get(a)
            key2 = subdict.get(a) + a[1:2]
            #print(key1, key2)
            newdict[key1] += cnts
            newdict[key2] += cnts
            #if the string exist in original poly, but isn't substituted, add to new one
            #this might never happen
        elif polydict[a] > 0:
            newdict[a] += polydict[a]
    return newdict

def fillpolydict(poly, polydict):
    i = 0
    j = 2
    while j < len(poly) + 1:
        polydict[poly[i:j]] += 1
        i += 1
        j += 1
    return

def countLetters(polydict):
    #only count the first letter, last letter of the poly will always be the same
    ans = {}
    for k, v in polydict.items():
        a = k[0:1]
        b = k[1:2]
        if ans.get(a):
            ans[a] += v
        else:
            ans[a] = v
    return ans

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    actpoly = fd.readline()
    actpoly = actpoly.strip()
    fd.readline()
    actsubs = fd.read().splitlines()
    fd.close

    fd = open('test.txt')
    tstpoly = fd.readline()
    tstpoly = tstpoly.strip()
    fd.readline()
    tstsubs = fd.read().splitlines()
    fd.close

    
    #make the subs into dictionaries
    tstsubs = convertSubs(tstsubs)
    actsubs = convertSubs(actsubs)

    #PART 2: store the counts of each pair
    tstpolydict = tstsubs.copy()
    actpolydict = actsubs.copy()
    for a in tstpolydict.keys():
        tstpolydict[a] = 0
    for a in actpolydict.keys():
        actpolydict[a] = 0

    #get the blank dicts
    tstblankpolydict = tstpolydict.copy()
    actblankpolydict = actpolydict.copy()
    #fill the polydict with the original poly
    print(tstpolydict)
    fillpolydict(tstpoly, tstpolydict)
    print(tstpolydict)
    #tstpolydict = subst2(tstpolydict, tstsubs, tstblankpolydict)
    for i in range(40):
        tstpolydict = subst2(tstpolydict, tstsubs, tstblankpolydict)
    print(tstpolydict)
    print(countLetters(tstpolydict))
    print('part2 actual stuff')
    fillpolydict(actpoly, actpolydict)
    for i in range(40):
        actpolydict = subst2(actpolydict, actsubs, actblankpolydict)
    print(countLetters(actpolydict))





    
def part1():
    #do the substituting
    for i in range(0):
        tstpoly = subst(tstpoly, tstsubs)
    print(len(list(tstpoly)))
    tstc = Counter(tstpoly)
    #print(tstc.most_common())

    for i in range(10):
        print(i)
        actpoly = subst(actpoly, actsubs)
    actc = Counter(actpoly)
    print(actc.most_common())

    return 0
    
    
