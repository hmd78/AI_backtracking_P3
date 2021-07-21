from checking1 import checking1
from checking3 import checking3
import time


def solve_puzzle(state, count):
    # print(state)
    counter = 0
    for k in range(count):
        for m in range(count):
            if isinstance(state[k][m], str):
                counter += 1

    if counter == count ** 2:
        # print('1  ', state)
        return True

    # MRV
    d = None
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
        cond = [checking1(state, count), checking3(state, count)]
        if cond[1] and cond[0] and solve_puzzle(state, count):
            # print('2  ', state)
            return True
        else:
            return False
    elif a is not None and b is not None:
        state[a][b] = '0'
        cond0 = [checking1(state, count), checking3(state, count)]
        if cond0[0] and cond0[1] and solve_puzzle(state, count):
            # print('3')
            return True
        state[a][b] = '1'
        cond1 = [checking1(state, count), checking3(state, count)]
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
checking1(p, n)
checking3(p, n)
# for i in range(n):
#     for j in range(n):
#         if isinstance(p[i][j], str):
#             # print('outer mac: ', i, j)
#             mac1(p, n, i, j)
# print(p)


if solve_puzzle(p, n):
    print("solution : ", p)
else:
    print("doesnt have answer")
print("--- %s seconds ---" % (time.time() - start_time))
