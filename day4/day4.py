def printboards(boards):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                print(boards[i][j][k][0], boards[i][j][k][1], end =" ")
            print('')
        print('\n')
#

def drawnum(num, boards):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if(boards[i][j][k][0] == num):
                    boards[i][j][k][1] = True
                    #print("found", num, "in board", i, "now:", boards[i][j][k][1])

def winnerboard(board):
    winner = False
    for i in range(5):
        #check horizontal
        winner = winner or (board[i][0][1] and board[i][1][1] and board[i][2][1] and board[i][3][1] and board[i][4][1])
        #check vertical
        winner = winner or (board[0][i][1] and board[1][i][1] and board[2][i][1] and board[3][i][1] and board[4][i][1])
    #check diagonals
    #winner = winner or (board[0][0][1] and board[1][1][1] and board[2][2][1] and board[3][3][1] and board[4][4][1])
    #winner = winner or (board[0][4][1] and board[1][3][1] and board[2][2][1] and board[3][1][1] and board[4][0][1])
    return winner

def winner (boards):
    for i in range(len(boards)):
        if (winnerboard(boards[i])):
            return i
    return -1
        
def createboards(lines):
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
    #print(boards)
    return boards

def boardscore(board):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j][1]:
                score += board[i][j][0]
    return score

def findnonwinning(boards):
    ans = list()
    for i in range(len(boards)):
        if not winnerboard(boards[i]):
            ans.append(boards[i])
    return ans

def findwinningboard(nums, board):
    print("finding a winning board")
    print(nums)
    for a in nums:
        #print("drawing number: ", a)
        drawnum(a, list(board))

        if(winnerboard(board)):
            print("boardscore of findwinningboard: ", boardscore(boards[win]))
            print("winning number: ", a)
            print("answer: ", a * boardscore(boards[win]))
            break
    print("finished finding a winning board")

if __name__ == '__main__':
    fd = open('input.txt')
    #get the number drawing order
    nums = fd.readline()
    #convert to a list of ints
    nums = list(map(int, (nums.split(','))))
    #print(nums)

    fd.readline() #get rid of blank line

    #get the rest of the input
    table = fd.read()
    table = table.split('\n')
    #get rid of blank lines
    lines = [i for i in table if i]
    #print(lines)

    #create the boards for next steps
    boards = createboards(lines)
    fd.close()
    boardspt2 = boards.copy()

    testboard1 = [[[1,False], [1,False], [1,False], [1,False], [1,False]],
                  [[1,False], [1,False], [1,False], [1,False], [1,False]],
                  [[1,False], [1,False], [1,False], [1,False], [1,False]],
                  [[1,False], [1,False], [1,False], [1,False], [1,False]],
                  [[1,False], [1,False], [1,False], [1,False], [1,False]]]

    testboard2 = [[[1,True], [1,False], [1,False], [1,False], [1,False]],
                  [[1,False], [1,True], [1,False], [1,False], [1,False]],
                  [[1,False], [1,False], [1,True], [1,False], [1,False]],
                  [[1,False], [1,False], [1,False], [1,True], [1,False]],
                  [[1,False], [1,False], [1,False], [1,False], [1,True]]]
       
    print("winner of testboard1: ", winnerboard(testboard1))
    print("winner of testboard2: ", winnerboard(testboard2))

    

    
    #PART 2
    wonboards = list()
    for a in nums:
        print("drawing number: ", a)
        drawnum(a, boards)

        nonwinning = list()
        nonwinning = findnonwinning(boards)
        
        if len(nonwinning) == 1:
            print("last board!")
            #findwinningboard(nums, nonwinning[0])
            #break
            print("boardscore of last winning board: ", boardscore(nonwinning[0]))            
            print("winning number: ", a)
            print("answer to part 2: ", a * boardscore(nonwinning[0]))
            printboards(nonwinning)




    """
        tmp = winner(boards)
        while (tmp != -1):
            wonboards.append(boards[tmp])
            del boards[tmp]
            tmp = winner(boards)
        #nonwinning = list()
        #nonwinning = findnonwinning(boardspt2)
    print(len(wonboards))
    printboards(wonboards)
    
         
        if len(nonwinning) == 2 or len(nonwinning) == 1:
            print("last board!")
            #findwinningboard(nums, nonwinning[0])
            #break
            print("boardscore of last winning board: ", boardscore(nonwinning[0]))
            print("boardscore of last winning board: ", boardscore(nonwinning[1]))
            print("winning number: ", a)
            print("answer to part 2: ", a * boardscore(nonwinning[0]))
            printboards(nonwinning)
            
    #printboards(boards)
    


    #last line in the last board
    #    80, 43, 75, 99, 79


    #PART 1
    #start drawing numbers
    for a in nums:
        #print("drawing number: ", a)
        drawnum(a, boards)

        win = winner(boards)
        if(win != -1):
            print("boardscore of winning board: ", boardscore(boards[win]))
            print("winning number: ", a)
            print("answer to part 1: ", a * boardscore(boards[win]))
            break

"""
