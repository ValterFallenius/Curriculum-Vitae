from math import acos


class Matrix():
    """Class of matrices."""
    def __init__(self, M=1, N=1, value=0):
        """Constructor creates an M by N matrix with only ones by default"""
        #if M < 0 or N < 0: raise ValueError("Matrix dimensions need to be non-negative integers.")
        
        self.size_M = M
        self.size_N = N
        self.matrix = []#Private!
        for i in range(self.size_M): # Traverses the rows
            self.matrix.append([value for j in range(self.size_N)]) # Creates the columns

    def transpose(self):
        """Transposes the matrix"""
        M = self.size_M
        N = self.size_N
        C = Matrix(N,M,0)

        for i in range(M): # Traverses the rows
            for j in range(N): # Traverses the columns
                C[j,i] = self[i,j]

        self = C
        return self
    def minmax(self):
        """Returns a tuple with minimum and maximium value in matrix."""
        mx = self[0,0]
        mn = mx
        for i in range(self.size_M):
            for j in range(self.size_N):
                if self[i,j] > mx: mx = self[i,j]
                if self[i,j] < mn: mn = self[i,j]
        return (mn,mx)

    def __getitem__(self,index):
        m,n = index
        return self.matrix[m][n]

    def __setitem__(self,index,value):
        m,n = index
        self.matrix[m][n] = value

    def __add__(self, B):
        """Addition with matrices, returns a third matrix"""
        self._dimcheck(B, "addition") #Makes sure matrices dimensions agree or raises ValueError

        #some variables
        M = self.size_M
        N = self.size_N
        #creates a new Matrix()-object
        C = Matrix(M,N,0)

        for i in range(M):
            for j in range(N):
                C[i,j] = self[i,j] + B[i,j]

        return C

    def __iadd__(self,B):
        """Adds B to self, updates self"""
        self = self + B
        return self

    def __sub__(self, B):
        """Subtract B from self, returns a third matrix"""
        B *= -1
        C = self + B
        return C

    def __isub__(self,B):
        """Subracts B from self, updates self"""
        self = self - B
        return self

    def __mul__(self,x):
        """Scalar or matrix product, depending on input x"""

        if isinstance(x,int) or isinstance(x,float):
            """Scales the matrix with an input factor x"""
            # Some variables
            M = self.size_M
            N = self.size_N
            C = Matrix(M,N)
            for i in range(M):
                for j in range(N): # Traverses the columns
                    C[i,j] = self[i,j] * x

        elif isinstance(x,Matrix):
            """Multiplies 2 matrices and returns the result."""
            self._dimcheck(x,"product")
            # Some variables
            M = self.size_M
            N = x.size_N
            length = self.size_N
            C = Matrix(N,M,0)

            for i in range(M):
                for j in range(N):
                    temp = [self[i,k]*x[k,j] for k in range(length)] # Sums the appropriate element for each coordinate.
                    C[i,j] = sum(temp)
        else:
            raise ValueError("invalid multiplication")
        return C

    def __imul__(self,x):
        """Scalar or matrix product depending on x, updates self"""
        self = self * x
        return self

    def __abs__(self):
        """Returns the norm of a vector"""
        self._dimcheck(None,"vector1")
        M = self.size_M
        N = self.size_N
        absolut = 0
        for i in range(M):
            for j in range(N):
                absolut += self[i,j]**2
        return absolut**0.5

    def __eq__(self,B):
        """Dunder method for equating 2 matrices"""
        if self.matrix == B.matrix:
            return True
        else:
            return False

    def __ne__(self,B):
        """Dunder method for non-equating 2 matrices"""
        if self.matrix == B.matrix:
            return False
        else:
            return True

    def __str__(self):
        """Returns the matrix in a pretty string"""

        #some variables
        M = self.size_M
        N = self.size_N
        minmax = self.minmax()
        string=""
        mx = max([len(str(minmax[0])),len(str(minmax[1]))])

        A = Matrix(M,N,0)
        #Converts self to a matrix A with strings of same length as elements.
        for i in range(M):
            for j in range(N):
                element = str(self[i,j])
                delta = mx - len(element)
                element = " "*(delta//2) + element + " "*(delta//2)
                if self[i,j] >= 0:
                    element = " " + element
                else:
                    element = element + " "
                if delta%2 == 1:
                    element += " "
                A[i,j] = element
        #Adds a space on the last column
        for i in range(M):
            A[i,N-1] += " "

        for i in range(M):
            string += "|"
            for j in range(N):
                string += str(A[i,j])
            string += "|\n"
        return string

    def angle_to(self,B):
        """Returns the angle between 2 vectors in radians. Ignores if they are column or row vectors"""
        self._dimcheck(B,"vector2")
        # Some variables
        mx = max([self.size_M,self.size_N])
        vec1 = self
        vec2 = B
        # Lines the vectors up for a dotproduct
        if self.size_M == mx:
            vec1 = vec1.transpose()
        if B.size_N == mx:
            vec2 = vec2.transpose()

        dotprod = vec1 * vec2

        dotprod = abs(dotprod)
        cosangle = dotprod/(abs(vec1)*abs(vec2))

        angle = acos(cosangle)
        return angle

    def _dimcheck(self,B = None,operation = "addition"):
        """Checks dimensions of self and B"""

        if operation == "addition": # If regular addition or subtraction matriced must have same dimensions
            if not(self.size_M == B.size_M and self.size_N == B.size_N):
                raise ValueError("Matrices {} and {} dimensions does not agree for addition/subtraction.".format("hej","hej"))#format(self.__name__, B.__name__))

        elif operation == "product":
            if not self.size_N == B.size_M:
                raise ValueError("Matrices {} and {} dimensions does not agree for a matrixproduct.".format("hej","hej"))#format(self.__name__, B.__name__))

        elif operation == "vector2":
            if not self._isvector() or not B._isvector():
                raise ValueError("{} and {} need both to be vectors".format("hej","hej"))#format(self.__name__, B.__name__))
            mx1 = max([self.size_M,self.size_N])
            mx2 = max([B.size_M,B.size_N])
            if not mx1 == mx2:
                raise ValueError("{} and {} does not have the same length".format("hej","hej"))#format(self.__name__, B.__name__))

        elif operation == "vector1":
            if not self._isvector():
                raise ValueError("{} need to be a vector".format("hej","hej"))#format(self.__name__))


    def _isvector(self):
        """returns true if self is vector (1xN or Mx1-matrix)."""
        if self.size_M == 1 or self.size_N == 1:
            return True
        return False

#---------------------------- Testkod ------------------------------------------
def test():

    A = Matrix(2,3,0)
    A[0, 0] = 1
    A[0, 1] = 2
    A[0, 2] = -1
    A[1, 0] = -1
    A[1, 1] = 1
    A[1, 2] = 3

    B = Matrix(3,2,0)
    B[0, 0] = 1
    B[0, 1] = 5
    B[1, 0] = 1
    B[1, 1] = 1
    B[2, 0] = 10
    B[2, 1] = 4

    AB = Matrix(2,2,0)
    AB[0, 0] = -7
    AB[0, 1] = 3
    AB[1, 0] = 30
    AB[1, 1] = 8

    noll = Matrix(2,2,0)

    assert A == A
    assert A.minmax() == (-1,3)
    assert B.minmax() == (1,10)
    assert A * B == AB
    assert AB - AB == noll
    assert A + A == A*2
    assert A * B != B * A

    vector1 = Matrix(1,3,0)
    vector1[0,0] = 1
    vector1[0,1] = 0
    vector1[0,2] = 1

    vector2 = Matrix(1,3,0)
    vector2[0,0] = 0
    vector2[0,1] = 1
    vector2[0,2] = 0

    assert abs(vector1) > 1.4
    assert abs(vector1) < 1.45
    assert abs(vector1.angle_to(vector1)) <1e-3
    assert abs(vector1.angle_to(vector2))-3.141592/2 <1e-4

    Aold = A
    A += A
    Bold = B
    B -= B

    assert A == Aold*2
    assert B == Bold*0


if __name__=='__main__':
    test()
