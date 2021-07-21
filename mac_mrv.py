import time
from mac1 import mac1
from mac3 import mac3


def solve_puzzle(state, count):
    print(state)
    counter = 0
    for k in range(count):
        for m in range(count):
            if isinstance(state[k][m], str):
                counter += 1

    if counter == count ** 2:
        # print('1  ', state)
        return True

    # MRV
    x = None
    y = None
    a = None
    b = None
    for i in range(n):
        for j in range(n):
            if isinstance(state[i][j], list) and len(state[i][j]) > 0:
                a, b = i, j
                if len(state[i][j]) == 1:
                    x, y = i, j

    if x is None and y is None and a is None and b is None:
        return False
    elif x is not None and y is not None:
        state[x][y] = state[x][y][0]
        cond = [mac1(state, count, x, y), mac3(state, count, x, y)]
        if cond[1] and cond[0] and solve_puzzle(state, count):
            # print('2  ', state)
            return True
        else:
            return False
    elif a is not None and b is not None:
        state[a][b] = '0'
        cond0 = [mac1(state, count, a, b), mac3(state, count, a, b)]
        if cond0[0] and cond0[1] and solve_puzzle(state, count):
            # print('3')
            return True
        state[a][b] = '1'
        cond1 = [mac1(state, count, a, b), mac3(state, count, a, b)]
        if cond1[0] and cond1[1] and solve_puzzle(state, count):
            # print('4')
            return True
        return False


n = int(input())

p = []
for i in range(n):
    tmp = input().split()
    p.append([x if x != '-' else ['0', '1'] for x in tmp])
print(p)
start_time = time.time()

if solve_puzzle(p, n):
    print("solution : ", p)
else:
    print("doesnt have answer")

print("--- %s seconds ---" % (time.time() - start_time))
print("finish")

