def det2(mat: list[list[float]]) -> float:
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

def trim_around(mat: list[list[float]], row: int, col: int) -> list[list[float]]:
    out_mat: list[list[float]] = []

    for i1, j1 in enumerate(mat):
        if i1 == row:
            continue

        tmp_mat: list[float] = []

        for i2, j2 in enumerate(j1):
            if i2 == col:
                continue

            tmp_mat.append(j2)
        
        out_mat.append(tmp_mat)
    
    return out_mat

def reduce(mat: list[list[float]]) -> list[list[list[float]]]:
    out_mat: list[list[list[float]]] = []

    for i in range(0, len(mat[0])):
        out_mat.append(trim_around(mat, 0, i))
    
    return out_mat

def flatten(mat: list[list[float]]) -> list[float]:
    out_mat: list[float] = []
    times: int = 1

    for i in mat[0]:
        out_mat.append(i * times)

        times *= -1
    
    return out_mat

def determinant(mat: list[list[float]]) -> float:
    row, col = len(mat), len(mat[0])
    
    if row == 2:
        return det2(mat)

    out_mat: list[float] = []

    reduced: list[list[list[float]]] = reduce(mat)
    flattened: list[float] = flatten(mat)

    for i in range(0, row):
        out_mat.append(flattened[i] * determinant(reduced[i]))
    
    return sum(out_mat)