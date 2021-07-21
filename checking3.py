def checking3(state, count):
    result = True
    for j in range(count):
        for k in range(count):
            if k < count - 2 and isinstance(state[j][k], str) and isinstance(state[j][k + 1], str) and state[j][k] == \
                    state[j][k + 1] and isinstance(state[j][k + 2], list) and state[j][k] in state[j][k+2]:
                state[j][k + 2].remove(state[j][k])
                if len(state[j][k + 2]) == 0:
                    result = False
            if j < count - 2 and isinstance(state[j][k], str) and isinstance(state[j + 1][k], str) and state[j][k] == \
                    state[j + 1][k] and isinstance(state[j + 2][k], list) and state[j][k] in state[j+2][k]:
                state[j + 2][k].remove(state[j][k])
                if len(state[j + 2][k]) == 0:
                    result = False
            if j > 1 and isinstance(state[j][k], str) and isinstance(state[j - 1][k], str) and state[j][k] == \
                    state[j - 1][k] and isinstance(state[j - 2][k], list) and state[j][k] in state[j-2][k]:
                state[j - 2][k].remove(state[j][k])
                if len(state[j - 2][k]) == 0:
                    result = False
            if k > 1 and isinstance(state[j][k], str) and isinstance(state[j][k - 1], str) and state[j][k] == \
                    state[j][k - 1] and isinstance(state[j][k - 2], list) and state[j][k] in state[j][k-2]:
                state[j][k - 2].remove(state[j][k])
                if len(state[j][k - 2]) == 0:
                    result = False
            if k < count - 2 and isinstance(state[j][k], str) and isinstance(state[j][k + 2], str) and state[j][k] == \
                    state[j][k + 2] and isinstance(state[j][k + 1], list) and state[j][k] in state[j][k+1]:
                state[j][k + 1].remove(state[j][k])
                if len(state[j][k + 1]) == 0:
                    result = False
            if j < count - 2 and isinstance(state[j][k], str) and isinstance(state[j + 2][k], str) and state[j][k] == \
                    state[j + 2][k] and isinstance(state[j + 1][k], list) and state[j][k] in state[j+1][k]:
                state[j + 1][k].remove(state[j][k])
                if len(state[j + 1][k]) == 0:
                    result = False
            if j > 1 and isinstance(state[j][k], str) and isinstance(state[j - 2][k], str) and state[j][k] == \
                    state[j - 2][k] and isinstance(state[j - 1][k], list) and state[j][k] in state[j-1][k]:
                state[j - 1][k].remove(state[j][k])
                if len(state[j - 1][k]) == 0:
                    result = False
            if k > 1 and isinstance(state[j][k], str) and isinstance(state[j][k - 2], str) and state[j][k] == \
                    state[j][k - 2] and isinstance(state[j][k - 1], list) and state[j][k] in state[j][k-1]:
                state[j][k - 1].remove(state[j][k])
                if len(state[j][k - 1]) == 0:
                    result = False
    return result

