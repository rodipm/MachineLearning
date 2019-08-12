# main.py

from Matrix import Matrix
from NeuralNetwork import NeuralNetwork
import math
import random

nn = NeuralNetwork(2, 3, 1)

train = True

dataset = {
    'inputs': 
        [[1, 1],
        [1, 0],
        [0, 1],
        [0, 0]], 
    'outputs':
        [[0],
        [1],
        [1],
        [0]]
}

while True:
    if train:
        for i in range(10000):
            index = math.floor(random.random() * 4)
            nn.train(dataset['inputs'][index], dataset['outputs'][index])

        if nn.predict([0, 0])[0] < 0.04 and nn.predict([1, 0])[0] > 0.98:
            train = False
    
    print(round(nn.predict([1, 1])[0]),
          round(nn.predict([0, 1])[0]),
          round(nn.predict([1, 0])[0]),
          round(nn.predict([0, 0])[0])
    )
    break
