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
    ans = 0
    #the first 3 bits of this pkt are the version number for this pkt
    ans += int(pkt[0:3], 2)
    
    #check if this pkt has more pkts in it
    #the next 3 bits are the type, which if it's 4 we're done
    if int(pkt[3:6], 2) != 4:
        #this pkt has more packets in it, must recurse
        if int(pkt[6:7], 2) == 0:
            #next 15 bits represent a number, which is the number of bits in the sub_pkts
            bits = int(pkt[7:22], 2)
            #pass those bits to an analyzing function, and add that ans to this ans
            ans += analyzeOp0Pkt(pkt[22:22+bits], bits)
        if int(pkt[6:7], 2) == 1:
            #next 11 bits represent a number, which is the number of sub-pkts following
            sbpkts = int(pkt[7:18], 2)
            #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
            tmp1, tmp2 = analyzeOp1Pkt(pkt[18:], sbpkts)
            ans += tmp1

    return ans

def analyzeOp0Pkt(pkts, totalBits):
    ans = 0
    currbit = 0
    #while there are still bits left to analyze:
    while currbit < totalBits:
        #add the version number to ans
        ans += int(pkts[currbit:currbit+3], 2)
        currbit += 3
        #check the pkt type
        if int(pkts[currbit:currbit+3], 2) != 4:
            #operator type pkt
            currbit += 3
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to op0 analyzing function, and add that ans to this ans
                ans += analyzeOp0Pkt(pkts[currbit:currbit+bits], bits)
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to op1 analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOp1Pkt(pkts[currbit:], sbpkts)
                ans += tmp
                currbit += bitsread
        else:
            currbit += 3
            #this is a literal value pkt
            while int(pkts[currbit:currbit+1], 2) == 1:
                currbit += 1
                #stuff here to analyze the actual number
                currbit += 4
            #last 5 bits of the pkt
            currbit += 1
            #stuff here to analyze last number portion
            currbit += 4
    return ans

def analyzeOp1Pkt(pkts, numpkts):
    ans = 0
    currbit = 0
    currpkt = 0
    while currpkt < numpkts:
        #analyze the next pkt
        currpkt += 1
        #add this pkt's version number to ans
        ans += int(pkts[currbit:currbit+3], 2)
        currbit += 3
        #check the pkt type
        if int(pkts[currbit:currbit+3], 2) != 4:
            #operator type pkt
            currbit += 3
            if int(pkts[currbit:currbit+1], 2) == 0:
                #next 15 bits represent a number, which is the number of bits in the sub_pkts
                currbit += 1
                bits = int(pkts[currbit:currbit+15], 2)
                currbit += 15
                #pass those bits to an analyzing function, and add that ans to this ans
                ans += analyzeOp0Pkt(pkts[currbit:currbit+bits], bits)
                currbit += bits
            else: #int(pkt[currbit:currbit+1], 2) == 1:
                #next 11 bits represent a number, which is the number of sub-pkts following
                currbit += 1
                sbpkts = int(pkts[currbit:currbit+11], 2)
                currbit += 11
                #pass the remaining bits to othe analyzing function, with the number of sub-pkts to analyze
                tmp, bitsread = analyzeOp1Pkt(pkts[currbit:], sbpkts)
                ans += tmp
                currbit += bitsread
        else:
            currbit += 3
            #this is a literal value pkt
            while int(pkts[currbit:currbit+1], 2) == 1:
                currbit += 1
                #stuff here to analyze the actual number
                currbit += 4
            #last 5 bits of the pkt
            currbit += 1
            #stuff here to analyze last number portion
            currbit += 4
            
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


    #test4 
    #test5 
    #test6
    #test7



