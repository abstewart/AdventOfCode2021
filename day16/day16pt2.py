import math
#Packet interpretation
#first 3 bits are the version number (don'y do anything w/ this currently
#next 3 bits are the pkt ID (4, 6, 3)

#if the pkt ID is a 4, it's a literal value
#following bits are parsed in sets of 5
#first bit is 1 if it's not the last set of 5, 0 otherwise
#the other 4 bits are the actual number portion
#all those bits add up to a number
#after that last packet, continue reading if necessary (will be a different pkt)

#if the pkt ID is not 4, it's a operator pkt
#next bit is either 1 or 0
#if length bit is 0: next 15 bits represent a number
#which is the number of bits in sub packets after that 15 bits
#after reading the indicated number of bits, parsing stops for this pkt

#if the length bit is 0, next 11 bits represent a number
#which is the number of sub-packets after those 11 bits
#after reading the indicated number of packets, parsing stops for this pkt


def expandHex(inp):
    ans = ''
    for a in inp:
        if a == '0':
            ans += '0000'
        elif a == '1':
            ans += '0001'
        elif a == '2':
            ans += '0010'
        elif a == '3':
            ans += '0011'
        elif a == '4':
            ans += '0100'
        elif a == '5':
            ans += '0101'
        elif a == '6':
            ans += '0110'
        elif a == '7':
            ans += '0111'
        elif a == '8':
            ans += '1000'
        elif a == '9':
            ans += '1001'
        elif a == 'A':
            ans += '1010'
        elif a == 'B':
            ans += '1011'
        elif a == 'C':
            ans += '1100'
        elif a == 'D':
            ans += '1101'
        elif a == 'E':
            ans += '1110'
        elif a == 'F':
            ans += '1111'
        else:
            print('Error in parsing hex input packet, invalid character')
            print('Current char: ', a)
            return none
    return ans





def analyzePktForVerNumSum(pkt):
    ans = []
    currbit = 0
    #the first 3 bits of this pkt are the version number for this pkt

    currbit += 3
    
    #check if this pkt has more pkts in it
    #the next 3 bits are the type, which if it's 4 we're done
    pktid = int(pkt[currbit:currbit+3], 2)
    currbit += 3
    if pktid == 0:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = sum(tmp1)
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = sum(tmp1)
    elif pktid == 1:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = math.prod(tmp1)
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = math.prod(tmp1)
    elif pktid == 2:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = min(tmp1)
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = min(tmp1)
    elif pktid == 3:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = max(tmp1)
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = max(tmp1)
    elif pktid == 5:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = 1 if tmp1[0] > tmp1[1] else 0
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = 1 if tmp1[0] > tmp1[1] else 0
    elif pktid == 6:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = 1 if tmp1[0] < tmp1[1] else 0
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = 1 if tmp1[0] < tmp1[1] else 0
    elif pktid == 7:
        #this pkt has more packets in it, must recurse
        if int(pkt[currbit:currbit+1], 2) == 0:
            currbit += 1
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[currbit:currbit+15], 2)
            currbit += 15
            #pass those bits to an analyzing function, and add that ans to this ans
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:currbit+bits], bits, False)
            ans = 1 if tmp1[0] == tmp1[1] else 0
        else: #int(pkt[6:7], 2) == 1:
            currbit += 1
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[currbit:currbit+11], 2)
            currbit += 11
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOpPkt(pkt[currbit:], sbpkts, True)
            ans = 1 if tmp1[0] == tmp1[1] else 0
    else:
        #this is a literal value pkt
        currbit = 6
        binval = ''
        while int(pkt[currbit:currbit+1], 2) == 1:
            currbit += 1
            binval += pkt[currbit:currbit+4]
            currbit += 4
        currbit += 1
        binval += pkt[currbit:currbit+4]
        currbit += 4
        ans = int(binval, 2)

    return ans

def analyzeOpPkt(pkts, cnt, op1):
    ans = []
    currbit = 0
    currpkt = 0
    while (currpkt if op1 else currbit) < cnt:
        #next pkt for loop
        currpkt += 1        
        currbit += 3
        #check the pkt type
        pktid = int(pkts[currbit:currbit+3], 2)
        currbit += 3
        if pktid == 0:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(sum(tmp1))
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(sum(tmp))
                currbit += bitsread
        elif pktid == 1:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(math.prod(tmp1))
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(math.prod(tmp))
                currbit += bitsread
        elif pktid == 2:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(min(tmp1))
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(min(tmp))
                currbit += bitsread
        elif pktid == 3:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(max(tmp1))
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(max(tmp))
                currbit += bitsread
        elif pktid == 5:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(1 if tmp1[0] > tmp1[1] else 0)
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(1 if tmp[0] > tmp[1] else 0)
                currbit += bitsread
        elif pktid == 6:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(1 if tmp1[0] < tmp1[1] else 0)
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(1 if tmp[0] < tmp[1] else 0)
                currbit += bitsread
        elif pktid == 7:
            #operator type pkt
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                tmp1, tmp2 = analyzeOpPkt(pkts[currbit:currbit+bits], bits, False)
                ans.append(1 if tmp1[0] == tmp1[1] else 0)
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOpPkt(pkts[currbit:], sbpkts, True)
                ans.append(1 if tmp[0] == tmp[1] else 0)
                currbit += bitsread
        else:
            binval = ''
            #this is a literal value pkt
            while int(pkts[currbit:currbit+1], 2) == 1:
                currbit += 1
                binval += pkts[currbit:currbit+4]
                currbit += 4
            #last 5 bits of the pkt
            currbit += 1
            binval += pkts[currbit:currbit+4]
            currbit += 4

            #add this number to the ans
            ans.append(int(binval, 2))
            
    return ans, currbit

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    fullpkt = fd.read().splitlines()
    fd.close

    print(fullpkt)
    pkt = expandHex(fullpkt[0])
    #print(pkt)
    print(analyzePktForVerNumSum(pkt))

    
    #test10 good
    #test11 good
    #test12 
    #test13

    #wrong answers:
    #12



