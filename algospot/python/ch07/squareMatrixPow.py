# [matrix class python]("http://code.activestate.com/recipes/578131-a-simple-matrix-class/")
# [identity,multiply]("https://rosettacode.org/wiki/Matrix-exponentiation_operator#Python")
from operator import mul
class Error(Exception):
    pass
class MatrixError(Error):
    def __init__(self,message):
        self.message = message

def identity(n):
    return [[(i==j)*1 for i in range(n)]for j in range(n)]
# Divide and Conquer   
def multiply(m1,m2):
    # ERROR HANDLING
    if len(m1)!=len(m2) or len(m1[0])!=len(m2[0]):
        raise MatrixError("NOT SQUARE MATRIX")
    #MULTIPLY
    return list(map(
        lambda row:
        list(map(
            lambda *column:
            sum(map(mul, row, column)),
            *m2)),
        m1))

def squareMartixPow(A,m):
    # BASE CONDITION
    if m==0: return identity(len(A))
    # even
    if m%2==0:half = squareMartixPow(A,m//2)
    # odd
    else: return multiply(squareMartixPow(A,m-1),A)
    return multiply(half,half)


if __name__=="__main__":
    A = [[1,2,3],[1,3],[1,2,3]]
    print(squareMartixPow(A,3))
