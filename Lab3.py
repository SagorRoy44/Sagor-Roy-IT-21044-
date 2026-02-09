import heapq

N = 3

row = [0, 0, -1, 1]
col = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    return board == goal

def manhattan(board):
    dist = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                goal_r = (val - 1) // N
                goal_c = (val - 1) % N
                dist += abs(i - goal_r) + abs(j - goal_c)
    return dist

def best_first(start_board, x, y):
    pq = []                      # priority queue
    visited = set()              # store visited boards

    h = manhattan(start_board)
    heapq.heappush(pq, (h, start_board, x, y, 0))   # (heuristic, board, blank_x, blank_y, depth)
    visited.add(tuple(map(tuple, start_board)))

    while pq:
        h, board, bx, by, depth = heapq.heappop(pq)

        if is_goal(board):
            print("Solution found at depth:", depth)
            return

        # expand 4 possible moves
        for i in range(4):
            nx = bx + row[i]
            ny = by + col[i]

            if is_valid(nx, ny):
                new_board = [r[:] for r in board]
                new_board[bx][by], new_board[nx][ny] = new_board[nx][ny], new_board[bx][by]

                t = tuple(map(tuple, new_board))
                if t not in visited:
                    visited.add(t)
                    new_h = manhattan(new_board)
                    heapq.heappush(pq, (new_h, new_board, nx, ny, depth + 1))

    print("No solution found.")

# Example run
start_board = [[1,2,3],
               [4,5,6],
               [7,0,8]]

best_first(start_board, 2, 1)
