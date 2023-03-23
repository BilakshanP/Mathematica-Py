import functions as funcs

class Matrix():
    def __init__(
            self,
            mat: list[list[float]] = [[]],
            row: int = 0,
            col: int = 0,

            is_lazy_initialized: bool = True,

            is_square: bool|None = None,
            is_identity: bool|None = None,

            determinant: float|None = None,
            transpose: list[list[float]]|None = None,
            minors:    list[list[float]]|None = None,
            cofactors: list[list[float]]|None = None,
            adjoint:   list[list[float]]|None = None,
            inverse:   list[list[float]]|None = None,
        ) -> None:
            __mat__: list[list[float]] = mat
            __row__: int = row
            __col__: int = col

            __is_lazy_initialized__: bool = is_lazy_initialized

            if is_lazy_initialized:
                __is_square__:   bool|None = is_square
                __is_identity__: bool|None = is_square

                __determinant__: float|None = determinant
                __transpose__:   list[list[float]]|None = transpose
                __minors__:      list[list[float]]|None = minors
                __cofactors__:   list[list[float]]|None = cofactors
                __adjoint__:     list[list[float]]|None = adjoint
                __inverse__:     list[list[float]]|None = inverse

                __is_up_to_date__: bool = False    

            else:
                __is_square__:   bool|None = (len(mat) == row) == (len(mat[0]) == col)
                __is_identity__: bool|None = funcs.is_identity(mat)

                if __is_identity__:
                    __determinant__: float|None = 1
                else:
                    __determinant__: float|None = funcs.determinant(mat)

                __transpose__:     list[list[float]]|None = funcs.transpose(mat, row, col)

                if __is_square__:
                    __minors__:    list[list[float]]|None = funcs.minors(mat, row, col)
                    __cofactors__: list[list[float]]|None = funcs.cofactors(mat, row, col)
                    __adjoint__:   list[list[float]]|None = funcs.transpose(__cofactors__, row, col)
                    if (__determinant__ == 0) or (__determinant__ == None):
                        __inverse__: list[list[float]]|None = None
                    else:
                        __inverse__: list[list[float]]|None = funcs.scalar_div(mat, row, col, __determinant__)

                __is_up_to_date__: bool = True

    @staticmethod
    def new():
        return Matrix()
    
    @staticmethod
    def new_from_mat_sized(vec: list[float], row: int, col: int, lazy_ini: bool = True):
        if (row < 0) or (col < 0):
            raise ValueError(f"\"row\" and \"col\" must have positive values but, {row} and {col} were provided.")

        if (len(vec) != row * col):
            raise ValueError(f"Vector of length {len(vec)} can't satisfy row * col = {row} * {col} = {row * col}")
    
        out_mat: list[list[float]] = []
        tmp_mat: list[float] = []

        for i in range(1, row * col + 1):
            tmp_mat.append(vec[i - 1])

            if i % col == 0:
                out_mat.append(tmp_mat)
                tmp_mat = []

        if lazy_ini:
            return Matrix(out_mat, row, col, lazy_ini)
        
        return Matrix(
            out_mat,
            row,
            col,
            False,
            row == col,
            funcs.is_identity(out_mat),
            funcs.determinant(out_mat),
            funcs.transpose(out_mat, row, col),
            )
    
    @staticmethod
    def new_from_mat_unsized(vec: list[list[float]], lazy_ini: bool = True):
        return Matrix(vec, len(vec), len(vec[0]), lazy_ini)

del funcs