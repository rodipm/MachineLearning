# NeuralNetwork.py
from Matrix import Matrix
import math

def sigmoid(num, i, j):
    return 1 / (1 + math.exp(-num))

def dsigmoid(num, i, j):
    return num * (1-num)

class NeuralNetwork:
    def __init__(self, i_nodes, h_nodes, o_nodes):
        self.i_nodes = i_nodes
        self.h_nodes = h_nodes
        self.o_nodes = o_nodes


        self.ih_biases = Matrix(self.h_nodes, 1)
        self.ih_biases.randomize()
        self.ho_biases = Matrix(self.o_nodes, 1)
        self.ho_biases.randomize()

        
        self.ih_weights = Matrix(self.h_nodes, self.i_nodes)
        self.ih_weights.randomize()
        self.ho_weights = Matrix(self.o_nodes, self.h_nodes)
        self.ho_weights.randomize()


        self.learning_rate = 0.1
    
    def train(self, arr, target):
        # INPUT => HIDDEN
        input = Matrix.array_to_matrix(arr)
        hidden = Matrix.multiply(self.ih_weights, input)
        hidden = Matrix.add(hidden, self.ih_biases)

        hidden.map(sigmoid)

        # HIDDEN => OUTPUT
        output = Matrix.multiply(self.ho_weights, hidden)
        output = Matrix.add(output, self.ho_biases)

        output.map(sigmoid)

        
        # BACKPROPAGATION

        # OUTPUT => HIDDEN
        expected = Matrix.array_to_matrix(target)
        output_error = Matrix.subtract(expected, output)
        d_output = Matrix.map(output, dsigmoid)
        hidden_T = Matrix.transpose(hidden)

        gradient = Matrix.hadamard(d_output, output_error)
        gradient = Matrix.scalar_multiply(gradient, self.learning_rate)

        # Apply to ho_biases
        self.ho_biases = Matrix.add(self.ho_biases, gradient)
        # Apply to ho_weights
        weights_ho_deltas = Matrix.multiply(gradient, hidden_T)
        self.ho_weights = Matrix.add(self.ho_weights, weights_ho_deltas)

        # HIDDEN => INPUT
        weights_ho_T = Matrix.transpose(self.ho_weights)
        hidden_error = Matrix.multiply(weights_ho_T, output_error)
        d_hidden = Matrix.map(hidden, dsigmoid)
        input_T = Matrix.transpose(input)

        gradient_H = Matrix.hadamard(d_hidden, hidden_error)
        gradient_H = Matrix.scalar_multiply(gradient_H, self.learning_rate)

        # Apply to ih_biases
        self.ih_biases = Matrix.add(self.ih_biases, gradient_H)
        # Apply to ih_weights
        weights_ih_deltas = Matrix.multiply(gradient_H, input_T)
        self.ih_weights = Matrix.add(self.ih_weights, weights_ih_deltas)

    def predict(self, arr):
        # INPUT => HIDDEN
        input = Matrix.array_to_matrix(arr)

        hidden = Matrix.multiply(self.ih_weights, input)
        hidden = Matrix.add(hidden, self.ih_biases)

        hidden.map(sigmoid)

        # HIDDEN => OUTPUT
        output = Matrix.multiply(self.ho_weights, hidden)
        output = Matrix.add(output, self.ho_biases)
        output.map(sigmoid)
        output = Matrix.matrix_to_array(output)

        return output