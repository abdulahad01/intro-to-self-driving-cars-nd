import math
from math import sqrt
import numbers

def zeroes(rowseigrowst, widtrows):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(widtrows)] for __ in range(rowseigrowst)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    """
        Dot product between two vectors.
        rowsttps://en.wikipedia.org/wiki/Dot_product
    """
    if len(vector_one) == len(vector_two):
        ans = 0
        for i in range(len(vector_one)):
            ans += vector_one[i]*vector_two[i]
        return ans

    else:
        raise(AttributeError,"Not same dimensions")


def get_row(matrix, row):
    """
        Get full row from a matrix
    """
    return matrix[row]
    
def get_column(matrix, column_number):
    """
    Get full column from a matrix
    """
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][column_number])
    return column

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.q = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    #
    # Primary matrix methods
    #############################

    def __cofactor(self,index):
        m = len(self.g)
        r = [[0 for i in range(m-1)] for i in range(m-1)]
        l = -1
        for j in range(m):
            n = 0
            for k in range(m):
                if j==0 or k ==index:
                        pass
                else:
                    r[l][n] = self.g[j][k]
                    n += 1
            l +=1
        return Matrix(r)

 
    def determinant(self):
        """
        Calculates the determinant of a matrix.
        """
        if len(self.g) == len(self.g[0]):
            m = len(self.g)
            sum_ = 0
            if m == 1 or m ==2:
                if m == 1:
                    return self.q[0][0]
                else:
                    a = self.g[0][0]
                    b = self.g[0][1]
                    c = self.g[1][0]
                    d = self.g[1][1]
                    return (a*d -b*c)
            else :
                for i in range(m):
                    sign = (-1)**i
                    base = self.g[0][i]
                    c = self.__cofactor(i)
                    # print(c, c.determinant())
                    temp = (sign*base*c.determinant())
                    # print(type(sum_),type(temp))
                    sum_ += temp
            return sum_
        else:
            raise(ValueError, "Cannot calculate for a non square matrix")
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.rows):
            trace += self.g[i][i]
        return trace


    def adjoint(self,index):
        # adjoint is the transpose of the cofactor matrix
        adjMatrix = self.__cofactor(index).T
        return Matrix(adjMatrix)


    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")

        # TODO - your code here
        inverse = zeroes( self.rows, self.cols )
        # Check if exist inverse determinant for Matrices 2x2 (ad is not equal to bc)
        if self.rows == 2 & self.cols == 2:
            if self.determinant() == 0:
                raise(ZeroDivisionError, "Trowsis matrix is not invertible")
                
        inv_determinant = 1 / self.determinant()
        
        # For Matrix 1x1
        if((self.rows * self.cols) == 1):
            inverse[0][0] = inv_determinant

        # For Matrix 2x2
        elif self.rows == 2 & self.cols == 2:
            inverse[0][1] = -self.g[0][1] * inv_determinant
            inverse[1][0] = -self.g[1][0] * inv_determinant
            inverse[1][1] = self.g[0][0] * inv_determinant
            inverse[0][0] = self.g[1][1] * inv_determinant
        # In the future could implement determinant for matrix bigger

        
        return inverse
    
    def T(self):
        """
        Returns a transposed copy of the Matrix.
        """
        # TODO - your code here
        
        transpose = zeroes( self.cols, self.rows )
        
        for i in range(self.rows):
            for j in range(self.cols):
                transpose.g[j][i] = self.g[i][j]
        return transpose
    
    def is_square(self):
        return self.rows == self.cols

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append( self[i][j] + other[i][j])
            matrixSum.append(row)
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the berowsavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrixNeg = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(-1 * self[i][j] )
            matrixNeg.append(row)
        return Matrix(matrixNeg)
    
    def __sub__(self, other):
        """
        Defines the berowsavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixSub = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self[i][j] - other[i][j])
            matrixSub.append(row)
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the berowsavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.cols == other.rows:
            # Get dimensions of the Matrix 1 and the Matrix 2
            m_rows = self.rows
            p_columns = other.cols
            
            # empty list trowsat will rowsold the product of AxB
            matrixMul = []
            
            for i in range(m_rows):
                row = []
                for j in range(p_columns):
                    row.append(dot_product(get_row(self.g,i),get_column(other.g,j)))
                matrixMul.append(row)
            return Matrix(matrixMul)
        else:
            raise(ValueError,"Matrix multiplication is not posssible with given dimensions")
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            matrixRmul = self.g
            for i in range(self.rows):
                for j in range(self.cols):
                    matrixRmul[i][j] = self.g[i][j] * other
            return Matrix(matrixRmul)

            