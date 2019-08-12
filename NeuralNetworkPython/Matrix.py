# Matrix.py
import random
import math
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for x in range(cols)] for y in range(rows)]


    @staticmethod
    def map(A, func):
        matrix = Matrix(A.rows, A.cols)
        matrix = matrix.map(func)
        return matrix
    
    def map(self, func):
        for i, arr in enumerate(self.data):
            for j, num in enumerate(arr):
               self.data[i][j] = func(num, i, j) 
        return self

    def randomize(self):
        self.map(lambda num, i, j: math.floor(random.random()*2 - 1))
        return self

    def print(self):
        print(self.data)
    
    @staticmethod
    def add(A, B):
        matrix = Matrix(A.rows, B.cols)
        matrix = matrix.map(lambda num, i, j: A.data[i][j] + B.data[i][j])
        return matrix

    @staticmethod
    def subtract(A, B):
        matrix = Matrix(A.rows, B.cols)
        matrix = matrix.map(lambda num, i, j: A.data[i][j] - B.data[i][j])
        return matrix

    @staticmethod
    def multiply(A, B):
        
        matrix = Matrix(A.rows, B.cols)

        def multiplyFunc(num, i, j):
            sum = 0
            for n in range(A.cols):
                prod = A.data[i][n] * B.data[n][j]    
                sum += prod
            return sum

        matrix = matrix.map(multiplyFunc)
        return matrix

    @staticmethod
    def array_to_matrix(arr):
        matrix = Matrix(len(arr), 1)
        matrix.map(lambda num, i, j: arr[i])
        return matrix

    @staticmethod
    def matrix_to_array(matrix):
        arr = []
        matrix.map(lambda num, i, j: arr.append(num))
        return arr

    @staticmethod
    def transpose(A):
        matrix = Matrix(A.cols, A.rows)
        matrix.map(lambda num, i, j: A.data[j][i])
        return matrix

    @staticmethod
    def scalar_multiply(A, scalar):
        matrix = Matrix(A.rows, A.cols)
        matrix.map(lambda num, i, j: A.data[i][j] * scalar)
        return matrix

    @staticmethod
    def hadamard(A, B):
        matrix = Matrix(A.rows, B.cols)
        matrix.map(lambda num, i, j: A.data[i][j] * B.data[i][j])
        return matrix
