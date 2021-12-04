def printboards(boards):
    
if __name__ == '__main__':
    fd = open('input.txt')
    nums = fd.readline()
    fd.readline() #get rid of blank line
    table = fd.read()
    table = table.split('\n')
    lines = [i for i in table if i]
    
    #print(lines)


    boards = list()
    board = list()
    line = list()
    i = 0
    while i < len(lines)/5:
        board = list()
        for j in range(5):
            a = lines[(i*5)+j]
            a = list(map(int, a.split()))
            line = list()
            for b in a:
                #attached to each number, indicate if it has been chosen or not
                line.append(list((b, False)))
                #print(line)
            board.append(line)
        boards.append(board)
        i += 1
    
    print(boards)
    fd.close()


    #    80, 43, 75, 99, 79
