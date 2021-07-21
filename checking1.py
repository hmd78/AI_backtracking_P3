def checking1(state, count):
    result = True
    for j in range(count):
        counter = [0, 0]
        for k in range(count):
            if isinstance(state[j][k], str) and state[j][k] == '0':
                counter[0] += 1
            if isinstance(state[j][k], str) and state[j][k] == '1':
                counter[1] += 1
        if counter[0] == count/2:
            [x.remove('0') for x in state[j] if isinstance(x, list) and '0' in x]
        if counter[1] == count/2:
            [x.remove('1') for x in state[j] if isinstance(x, list) and '1' in x]

    for k in range(count):
        counter = [0, 0]
        for j in range(count):
            if isinstance(state[j][k], str) and state[j][k] == '0':
                counter[0] += 1
            if isinstance(state[j][k], str) and state[j][k] == '1':
                counter[1] += 1
        if counter[0] == count/2:
            [state[x][k].remove('0') for x in range(count) if isinstance(state[x][k], list) and '0' in state[x][k]]
        if counter[1] == count/2:
            [state[x][k].remove('1') for x in range(count) if isinstance(state[x][k], list) and '1' in state[x][k]]

    for k in range(count):
        for m in range(count):
            if isinstance(state[k][m], list) and len(state[k][m]) == 0:
                result = False

    return result
