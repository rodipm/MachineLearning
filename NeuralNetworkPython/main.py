# main.py

from Matrix import Matrix
from NeuralNetwork import NeuralNetwork

m1 = Matrix(3, 2)
m2 = Matrix(3, 2)
print(m1.data)
print(m2.data)
print(Matrix.sum(m1, m2).data)

