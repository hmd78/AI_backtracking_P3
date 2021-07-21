def normalize(tmp_state, count, c, d):
    for j in range(count):
        if isinstance(tmp_state[c][j], list) and len(tmp_state[c][j]) == 1:
            tmp_state[c][j] = tmp_state[c][j][0]
        if isinstance(tmp_state[j][d], list) and len(tmp_state[j][d]) == 1:
            tmp_state[j][d] = tmp_state[j][d][0]
