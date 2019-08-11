# Matrix.py
import random
import math
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[math.floor(random.random()*10)] * cols] * rows
        self.data = [[math.floor(random.random()*10) for x in range(cols)] for y in range(rows)]
       
    @staticmethod
    def array_to_matrix(arr):
        matrix = Matrix(len(arr), 1)
        print(matrix.data)
        matrix.map(lambda num, i, j: print(i, j, num))
        return matrix

    def map(self, func):
        for i, arr in enumerate(self.data):
            for j, num in enumerate(arr):
               self.data[i][j] = func(num, i, j) 
        return self

    @staticmethod
    def sum(A, B):
        matrix = Matrix(A.rows, B.cols)
        matrix = matrix.map(lambda num, i, j: A.data[i][j] + B.data[i][j])
        return matrix
