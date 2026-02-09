from collections import deque

N = 3

class p8_board:
    def __init__(self, board, x, y, depth):
        self.board = board
        self.x = x
        self.y = y
        self.depth = depth

row = [0, 0, -1, 1]
column = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def is_goal(board):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return goal == board

def breadthFS(start, x, y):
    queue = deque()
    visited = set()

    queue.append(p8_board(start, x, y, 0))
    visited.add(tuple(map(tuple, start)))

    while queue:
        current = queue.popleft()

        if is_goal(current.board):
            print(f"Solution found at current depth {current.depth}")
            return

        for i in range(4):
            new_x = current.x + row[i]
            new_y = current.y + column[i]
            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current.board]

                new_board[current.x][current.y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current.x][current.y]

                board_tuple = tuple(map(tuple, new_board))

                if board_tuple not in visited:
                    visited.add(board_tuple)
                    queue.append(p8_board(new_board, new_x, new_y, current.depth + 1))

    print("No solution found")


# Test BFS
start_board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
x, y = 2, 1
breadthFS(start_board, x, y)
