import copy
from normalize import normalize


def mac3(state, count, c, d):
    # print("mac : ", c, d)
    tmp_state = copy.deepcopy(state)
    normalize(tmp_state, count, c, d)
    for j in range(count):
        if j < count - 2 and isinstance(tmp_state[c][j], str) and isinstance(tmp_state[c][j + 1], str) and \
                tmp_state[c][j] == tmp_state[c][j + 1] and isinstance(state[c][j + 2], list) and\
                tmp_state[c][j] in state[c][j + 2]:
            # print('1', c, j+2)
            state[c][j + 2].remove(tmp_state[c][j])
            if len(state[c][j + 2]) == 0:
                return False
            if not mac3(state, count, c, j+2):
                return False
        if j < count - 2 and isinstance(tmp_state[j][d], str) and isinstance(tmp_state[j + 1][d], str) and\
                tmp_state[j][d] == tmp_state[j + 1][d] and isinstance(state[j + 2][d], list) and\
                tmp_state[j][d] in state[j + 2][d]:
            # print('2', j+2, d)
            state[j + 2][d].remove(tmp_state[j][d])
            if len(state[j + 2][d]) == 0:
                return False
            if not mac3(state, count, j+2, d):
                return False
        if j > 1 and isinstance(tmp_state[j][d], str) and isinstance(tmp_state[j - 1][d], str) and tmp_state[j][d] == \
                tmp_state[j - 1][d] and isinstance(state[j - 2][d], list) and tmp_state[j][d] in state[j - 2][d]:
            # print('3', j-2, d)
            state[j - 2][d].remove(tmp_state[j][d])
            if len(state[j - 2][d]) == 0:
                return False
            if not mac3(state, count, j-2, d):
                return False
        if j > 1 and isinstance(tmp_state[c][j], str) and isinstance(tmp_state[c][j - 1], str) and tmp_state[c][j] == \
                tmp_state[c][j - 1] and isinstance(state[c][j - 2], list) and tmp_state[c][j] in state[c][j - 2]:
            # print(state)
            # print(tmp_state)
            # print('4', c, j-2)
            state[c][j - 2].remove(tmp_state[c][j])
            if len(state[c][j - 2]) == 0:
                return False
            if not mac3(state, count, c, j-2):
                return False
        if j < count - 2 and isinstance(tmp_state[c][j], str) and isinstance(tmp_state[c][j + 2], str) and \
                tmp_state[c][j] == tmp_state[c][j + 2] and isinstance(state[c][j + 1], list) and\
                tmp_state[c][j] in state[c][j + 1]:
            # print('5', c, j+1)
            state[c][j + 1].remove(tmp_state[c][j])
            if len(state[c][j + 1]) == 0:
                return False
            if not mac3(state, count, c, j+1):
                return False
        if j < count - 2 and isinstance(tmp_state[j][d], str) and isinstance(tmp_state[j + 2][d], str) and\
                tmp_state[j][d] == tmp_state[j + 2][d] and isinstance(state[j + 1][d], list) and\
                tmp_state[j][d] in state[j + 1][d]:
            # print(state)
            # print(tmp_state)
            # print('6', j+1, d)
            state[j + 1][d].remove(tmp_state[j][d])
            if len(state[j + 1][d]) == 0:
                return False
            if not mac3(state, count, j+1, d):
                return False
        if j > 1 and isinstance(tmp_state[j][d], str) and isinstance(tmp_state[j - 2][d], str) and tmp_state[j][d] == \
                tmp_state[j - 2][d] and isinstance(state[j - 1][d], list) and tmp_state[j][d] in state[j - 1][d]:
            # print('7', j-1, d)
            state[j - 1][d].remove(tmp_state[j][d])
            if len(state[j - 1][d]) == 0:
                return False
            if not mac3(state, count, j-1, d):
                return False
        if j > 1 and isinstance(tmp_state[c][j], str) and isinstance(tmp_state[c][j - 2], str) and tmp_state[c][j] == \
                tmp_state[c][j - 2] and isinstance(state[c][j - 1], list) and tmp_state[c][j] in state[c][j - 1]:
            # print('8', c, j-1)
            state[c][j - 1].remove(tmp_state[c][j])
            if len(state[c][j - 1]) == 0:
                return False
            if not mac3(state, count, c, j-1):
                return False
    return True
