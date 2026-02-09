import copy

N = 3
row = [0, 0, -1, 1]  # left, right, up, down
col = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1,2,3],[4,5,6],[7,8,0]]
    return board == goal

def manhattan(board):
    h = 0
    for i in range(N):
        for j in range(N):
            val = board[i][j]
            if val != 0:
                gr = (val - 1) // N
                gc = (val - 1) % N
                h += abs(i - gr) + abs(j - gc)
    return h

def hill_climbing(start_board, x, y):
    current = start_board
    cx, cy = x, y
    steps = 0

    while True:
        if is_goal(current):
            print("Goal reached in", steps, "steps")
            return

        neighbors = []

        # Generate all possible moves
        for i in range(4):
            nx, ny = cx + row[i], cy + col[i]
            if is_valid(nx, ny):
                new_board = copy.deepcopy(current)
                new_board[cx][cy], new_board[nx][ny] = new_board[nx][ny], new_board[cx][cy]
                neighbors.append((manhattan(new_board), new_board, nx, ny))

        # Choose the neighbor with the lowest heuristic
        neighbors.sort(key=lambda x: x[0])
        best_h, best_board, best_x, best_y = neighbors[0]

        # If no improvement, we are stuck (local maxima)
        if best_h >= manhattan(current):
            print("Stuck at local maxima. Steps:", steps)
            return

        current, cx, cy = best_board, best_x, best_y
        steps += 1

# Example
start_board = [[1,2,3],
               [4,5,6],
               [7,0,8]]

hill_climbing(start_board, 2, 1)
