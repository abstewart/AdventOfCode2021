import heapq
import sys
#currently only check the lower one and right one
def findshortestpath(grid, path, cur, dest, leng):
    cur[0] = x
    cur[1] = y
    if cur != (0,0):
        leng += grid[x][y]

    if cur == dest:
        return leng
    
    while cur != (len(grid)-1, len(grid)-1):
        path.append(cur)
        leng += grid[cur[0]][cur[1]]
        if cur[0] == len(grid)-1:
            cur = (cur[0], cur[1]+1)
        elif cur[1] == len(grid)-1:
            cur = (cur[0]+1, cur[1])
        else:
            if grid[cur[0]][cur[1]+1] < grid[cur[0]+1][cur[1]]:
                cur = (cur[0], cur[1]+1)
            elif grid[cur[0]+1][cur[1]] < grid[cur[0]][cur[1]+1]:
                cur = (cur[0]+1, cur[1])
            else:
                #both are same value
                return leng
    return leng

def makeDistances(grid):
    ans = dict()
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            nodes.append((i,j))
            tmp = {}
            if i == 0:
                if j == 0:
                    #2 pts
                    tmp[(i+1,j)] = grid[i+1][j]
                    tmp[(i,j+1)] = grid[i][j+1]
                elif j == len(grid)-1:
                    #2 pts
                    tmp[(i+1,j)] = grid[i+1][j]
                    tmp[(i,j-1)] = grid[i][j-1]
                else:
                    #3 pts
                    tmp[(i+1,j)] = grid[i+1][j]
                    tmp[(i,j+1)] = grid[i][j+1]
                    tmp[(i,j-1)] = grid[i][j-1]
            elif i == len(grid)-1:
                if j == 0:
                    #2 pts
                    tmp[(i-1,j)] = grid[i-1][j]
                    tmp[(i,j+1)] = grid[i][j+1]
                elif j == len(grid)-1:
                    #2 pts
                    tmp[(i-1,j)] = grid[i-1][j]
                    tmp[(i,j-1)] = grid[i][j-1]
                else:
                    #3 pts
                    tmp[(i-1,j)] = grid[i-1][j]
                    tmp[(i,j+1)] = grid[i][j+1]
                    tmp[(i,j-1)] = grid[i][j-1]
            else:
                if j == 0:
                    #3 pts
                    tmp[(i+1,j)] = grid[i+1][j]
                    tmp[(i-1,j)] = grid[i-1][j]
                    tmp[(i,j+1)] = grid[i][j+1]
                elif j == len(grid)-1:
                    #3 pts
                    tmp[(i+1,j)] = grid[i+1][j]
                    tmp[(i-1,j)] = grid[i-1][j]
                    tmp[(i,j-1)] = grid[i][j-1]
                else:
                    #4 pts
                    tmp[(i+1,j)] = grid[i+1][j]
                    tmp[(i-1,j)] = grid[i-1][j]
                    tmp[(i,j+1)] = grid[i][j+1]
                    tmp[(i,j-1)] = grid[i][j-1]
            ans[(i,j)] = tmp
    return ans, nodes

def makeDistances2(grid):
    ans = dict()
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            nodes.append((i,j))
            tmp = []
            if i == 0:
                if j == 0:
                    #2 pts
                    tmp.append(((i+1,j), grid[i+1][j]))
                    tmp.append(((i,j+1), grid[i][j+1]))
                elif j == len(grid)-1:
                    #2 pts
                    tmp.append(((i+1,j), grid[i+1][j]))
                    tmp.append(((i,j-1), grid[i][j-1]))
                else:
                    #3 pts
                    tmp.append(((i+1,j), grid[i+1][j]))
                    tmp.append(((i,j+1), grid[i][j+1]))
                    tmp.append(((i,j-1), grid[i][j-1]))
            elif i == len(grid)-1:
                if j == 0:
                    #2 pts
                    tmp.append(((i-1,j), grid[i-1][j]))
                    tmp.append(((i,j+1), grid[i][j+1]))
                elif j == len(grid)-1:
                    #2 pts
                    tmp.append(((i-1,j), grid[i-1][j]))
                    tmp.append(((i,j-1), grid[i][j-1]))
                else:
                    #3 pts
                    tmp.append(((i-1,j), grid[i-1][j]))
                    tmp.append(((i,j+1), grid[i][j+1]))
                    tmp.append(((i,j-1), grid[i][j-1]))
            else:
                if j == 0:
                    #3 pts
                    tmp.append(((i+1,j), grid[i+1][j]))
                    tmp.append(((i-1,j), grid[i-1][j]))
                    tmp.append(((i,j+1), grid[i][j+1]))
                elif j == len(grid)-1:
                    #3 pts
                    tmp.append(((i+1,j), grid[i+1][j]))
                    tmp.append(((i-1,j), grid[i-1][j]))
                    tmp.append(((i,j-1), grid[i][j-1]))
                else:
                    #4 pts
                    tmp.append(((i+1,j), grid[i+1][j]))
                    tmp.append(((i-1,j), grid[i-1][j]))
                    tmp.append(((i,j+1), grid[i][j+1]))
                    tmp.append(((i,j-1), grid[i][j-1]))
            ans[(i,j)] = tmp
    return ans, nodes
def dijkstra(g, s, t):

    q = []
    d = {k: sys.maxsize for k in g.keys()}
    p = {}

    d[s] = 0 
    heapq.heappush(q, (0, s))

    while q:
        last_w, curr_v = heapq.heappop(q)
        for n, n_w in g[curr_v]:
            cand_w = last_w + n_w # equivalent to d[curr_v] + n_w 
            # print d # uncomment to see how deltas are updated
            if cand_w < d[n]:
                d[n] = cand_w
                p[n] = curr_v
                heapq.heappush(q, (cand_w, n))

    #print ("predecessors: ", p )
    #print ("delta: ", d )
    return d[t]

if __name__ == '__main__':
    #format the input
    fd = open('input.txt')
    grid = fd.read().splitlines()
    fd.close

    #format each line as a list of ints
    for i, a in enumerate(grid):
        grid[i] = [int(digit) for digit in a]
    #print the grid
    #print(grid)

    #make the pt2 grid:
    #copy the grid over (in the y dir)
    grid2 = grid.copy()
    for i, a in enumerate(grid2):
        tmp = a.copy()
        for j in range(4):
            tmp = tmp + [b+j-8 if b+1+j > 9 else b+1+j for b in a]
        grid2[i] = tmp
    #copy the grid over (in the y dir)

    for i in range(4):
        for j in range(len(grid)):
            tmp = grid2[i*len(grid)+j]
            tmp = [1 if b+1 == 10 else b+1 for b in tmp]
            grid2.append(tmp)
    #print(grid2)
    #print(len(grid2))
    #print(len(grid2[0]))
  

    
    #make a graph of the input
    nodes = []
    distances = dict()
    
    distances, nodes = makeDistances2(grid2)

    #print(distances)
    print('starting the algo')
    print(dijkstra(distances, (0,0), (499,499)))
    
    #print(visited)
    #print('test ans: ', visited[(9,9)])

    #part 2
    #print('testing ans pt2: ', visited[(49,49)])
    #print('act ans pt 2: ', visited[(499,499)])
    
    
