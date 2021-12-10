open_list = ['(', '[', '{', '<']
close_list = [')', ']', '}', '>']
#returns 0 for valid syntax
#returns -1 for incomplete
#returns score of illegal character if found
def checkSyntax(mystr):
    stack = []
    for a in mystr:
        if a in open_list:
            stack.append(a)
        elif a in close_list:
            b = stack.pop(len(stack)-1)
            if not close_list.index(a) == open_list.index(b):
                #illegal closing, return score
                if a == ')':
                    return -1, 3
                elif a == ']':
                    return -1, 57
                elif a == '}':
                    return -1, 1197
                elif a == '>':
                    return -1, 25137
    if len(stack) > 0:
        score = 0
        while len(stack) > 0:
            #get the last element of the stack
            a = stack.pop(len(stack)-1)
            score *= 5
            if a == '(':
                score += 1
            if a == '[':
                score += 2
            if a == '{':
                score += 3
            if a == '<':
                score += 4
        #incomplete syntax case
        return 0, score
    #good syntax, doesn't actually exist
    return 0

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    inputs = fd.readlines()
    fd.close

    fd = open('test.txt')
    tin = fd.readlines()
    fd.close

    #format the inputs
    for i in range(len(tin)):
        tin[i] = tin[i].strip()
    for i in range(len(inputs)):
        inputs[i] = inputs[i].strip()
    print(tin)

    if -1:
        print('-1 counts')
    
    p1ans = 0
    p2ans = list()
    for a in tin:
        ck, tmp = checkSyntax(a)
        if ck == -1:
            p1ans += tmp
        if ck == 0:
            p2ans.append(tmp)
    print('part1 testing answer: ', p1ans)
    p2ans.sort()
    print('part2 testing answer: ', p2ans[int(len(p2ans)/2 - 0.5)])

    p1ans = 0
    p2ans = list()
    print(p2ans)
    for a in inputs:
        ck, tmp = checkSyntax(a)
        if ck == -1:
            p1ans += tmp
        if ck == 0:
            p2ans.append(tmp)
    print('part1 actual answer: ', p1ans)
    p2ans.sort()
    print('part2 actual answer: ', p2ans[int(len(p2ans)/2 - 0.5)])
    #print('part2 actual answer: ', p2ans)

    
