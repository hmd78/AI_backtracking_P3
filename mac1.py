import copy
from normalize import normalize


def mac1(state, count, c, d):
    tmp_state = copy.deepcopy(state)
    row = [0, 0]
    column = [0, 0]
    normalize(tmp_state, count, c, d)
    for h in range(count):
        if isinstance(tmp_state[c][h], str) and tmp_state[c][h] == '0':
            row[0] += 1
        if isinstance(tmp_state[c][h], str) and tmp_state[c][h] == '1':
            row[1] += 1
        if isinstance(tmp_state[h][d], str) and tmp_state[h][d] == '0':
            column[0] += 1
        if isinstance(tmp_state[h][d], str) and tmp_state[h][d] == '1':
            column[1] += 1
    # print(row, c, d)
    # print(column, c, d)

    if row[0] == row[1] and column[0] == column[1]:
        return True

    # print(state)
    if row[0] == count/2:
        for x in range(count):
            if isinstance(state[c][x], list) and '0' in state[c][x] and len(state[c][x]) == 2:
                # print('row 0 before', state)
                state[c][x].remove('0')
                # print('row 0 after', state)
                if not mac1(state, count, c, x):
                    return False
    elif row[0] > count/2:
        return False
    if row[1] == count/2:
        for x in range(count):
            if isinstance(state[c][x], list) and '1' in state[c][x] and len(state[c][x]) == 2:
                # print('row 1 bfr', state)
                state[c][x].remove('1')
                # print('row 1 aft', state)
                if not mac1(state, count, c, x):
                    return False
    elif row[1] > count/2:
        return False

    if column[0] == count/2:
        for x in range(count):
            if isinstance(state[x][d], list) and '0' in state[x][d] and len(state[x][d]) == 2:
                # print('column 0 bfr', state)
                state[x][d].remove('0')
                # print('column 0 aft', state)
                if not mac1(state, count, x, d):
                    return False
    elif column[0] > count/2:
        return False
    if column[1] == count/2:
        for x in range(count):
            if isinstance(state[x][d], list) and '1' in state[x][d] and len(state[x][d]) == 2:
                # print('column 1 bfr', state)
                state[x][d].remove('1')
                # print('column 1 aft', state)
                if not mac1(state, count, x, d):
                    return False
    elif column[1] > count/2:
        return False
    return True

