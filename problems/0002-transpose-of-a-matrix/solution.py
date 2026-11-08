def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    return [list(col) for col in zip(*a)]
    # new_col_length = len(a)
    # m = [[0] * new_col_length for _ in range(len(a[0]))]
    # for idx, row in enumerate(a):
    #     for elx, el in enumerate(row):
    #         m[elx][idx] = el
    # return m