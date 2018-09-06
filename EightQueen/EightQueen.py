import sys
import time


class UsedElements:
    solutions = []

    def __init__(self):
        self.rows = []
        self.cols = []
        self.points = []

    def is_valid(self, x, y):
        if x in self.cols:
            return False
        if y in self.rows:
            return False
        for point in self.points:
            if abs(x - point[0]) - abs(y - point[1]) == 0:
                return False
        return True

    @staticmethod
    def add_solution(x):
        r = x.copy()
        r.sort()
        if r not in UsedElements.solutions:
            UsedElements.solutions.append(r)


def print_board(n, s):
    board = [[0] * n for _ in range(n)]
    for p in s:
        board[p[1]][p[0]] = 1
    for r in board:
        print(r)
    print('---------------')


def get_solutions(n, board_size, elements):
    if n <= 0:
        UsedElements.add_solution(elements.points)
        return
    start_iterations = board_size - n
    max_iterations = min(int(board_size / 2) + start_iterations, board_size)
    for x in range(start_iterations, max_iterations):
        for y in range(board_size):
            if elements.is_valid(x, y):
                elements.cols.append(x)
                elements.rows.append(y)
                elements.points.append([x, y])
                get_solutions(n - 1, board_size, elements)
                elements.cols.remove(x)
                elements.rows.remove(y)
                elements.points.remove([x, y])


def solve(n):
    if n <= 0:
        return
    used_elements = UsedElements()
    t0 = time.time()
    get_solutions(n, n, used_elements)
    t1 = time.time()
    t = t1 - t0
    for r in UsedElements.solutions:
        print_board(n, r)

    print("Found %d solutions in %.2f seconds" % (len(UsedElements.solutions), t))


if __name__ == "__main__":
    args = sys.argv
    n = int(args[1])
    solve(n)
