import math

def gamma(inp):
    ans = list()
    for i in range(len(inp[0])-1):
        ans.append(0)
    for a in inp:
        a.split()
        for b in range(len(a)):
            if a[b] == '1':
                ans[b] += 1
    for i in range(len(inp[0])-1):
        ans[i] = round(ans[i] / len(inp))

    return ans
                

def mod_bit(i, inp):
    cnt = 0
    for a in inp:
        a.split()
        if(a[i] == '1'):
            cnt += 1
    #print(cnt, len(inp))
    if(cnt >= (len(inp)/2)):
       return 1
    else:
       return 0

def filt(i, k, inp):
    ans = inp
    ind = 0
    while ind < len(ans):
        a = ans[ind]
        a.split()
        if(a[i] != k):
            del ans[ind]
            ind -= 1
        ind += 1
#            print('removing: ', a)
    return ans

if __name__ == '__main__':
    fd = open('input.txt')
    lines = fd.readlines()
    fd.close()
    
    print(gamma(lines))
    #654 & 3441
    print(654*3441)

    #finding the oxygen
    oxy = lines.copy()
    co2 = lines.copy()

    #co2 = lines
    c = 0
    #print(co2)
    #110101110000 | 3440
    #110001001001 | 3145
    while len(co2) > 1 and c < 12:
        #print(len(co2))
        tmp = str(mod_bit(c, co2))
        if tmp == '1':
            tmp = '0'
        else:
            tmp = '1'
        #print(tmp, c)
        filt(c, tmp, co2)
        #print(co2)
        c += 1
    print(co2)

    c = 0
    #print(oxy)
    #011110001111 | 1935
    while len(oxy) > 1 and c < 12:
        #print(len(oxy))
        tmp = str(mod_bit(c, oxy))
        #print(tmp, c)
        filt(c, tmp, oxy)
        #print(oxy)
        c += 1
    print(oxy)

    print(3145 * 1935)
