import inner

#def is_square(row, col) -> bool:
#    return row == col

def is_identity(vec: list[list[float]]) -> bool:
    if len(vec) != len(vec[0]):
        return False

    for i1, j1 in enumerate(vec):
        for i2, j2 in enumerate(j1):
            if ((i1 != i2) and (j2 == 0)) or (j2 == 1):
                pass
            else:
                return False
    
    return True

def determinant(mat: list[list[float]]) -> float|None:
    row, col = len(mat), len(mat[0])

    if row != col:
        return None

    if row == 1:
        return mat[0][0]
    
    if row == 2:
        return inner.det2(mat)

    out_mat: list[float] = []

    reduced: list[list[list[float]]] = inner.reduce(mat)
    flattened: list[float] = inner.flatten(mat)

    for i in range(0, row):
        out_mat.append(flattened[i] * inner.determinant(reduced[i]))
    
    return sum(out_mat)

def transpose(mat: list[list[float]], row: int, col: int) -> list[list[float]]|None:
    if row == 0:
        return None

    out_mat: list[list[float]] = []

    for i in range(0, row):
        tmp_mat: list[float] = []

        for j in mat:
            tmp_mat.append(j[i])

        out_mat.append(tmp_mat)
    
    return out_mat

def minors(mat: list[list[float]], row: int, col: int) -> list[list[float]]:
    out_mat: list[list[float]] = []

    for i in range(0, row):
        tmp_mat: list[float] = []

        for j in range(0, col):
            tmp_mat.append(inner.determinant(inner.trim_around(mat, i, j)))
        
        out_mat.append(tmp_mat)
    
    return out_mat

def cofactors(mat: list[list[float]], row: int, col: int) -> list[list[float]]:
    out_mat: list[list[float]] = []
    times: int = 1

    for i1, j1 in enumerate(minors(mat, row, col)):
        tmp_mat: list[float] = []

        for i2, j2 in enumerate(j1):
            tmp_mat.append(j2 * times)

            times *= -1
        
        out_mat.append(tmp_mat)
    
    return out_mat

def scalar_mul(mat: list[list[float]], row: int, col: int, scalar: float) -> list[list[float]]:
    out_mat: list[list[float]] = []

    for i in range(0, row):
        tmp_mat: list[float] = []

        for j in range(0, col):
            tmp_mat.append(mat[i][j] * scalar)
        
        out_mat.append(tmp_mat)
    
    return out_mat

def scalar_div(mat: list[list[float]], row: int, col: int, scalar: float) -> list[list[float]]:
    return scalar_mul(mat, row, col, 1/scalar)