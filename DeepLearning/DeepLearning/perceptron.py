# -*- coding: utf-8 -*-

"""

@Time       :19-7-22 下午7:05
@Author     :FfanWang
@Description:Learning and coding of perceptron

"""

from __future__ import print_function
from functools import reduce


class VectorOP(object):

    # dot multiply function
    def dot(x, y):
        return reduce(lambda a, b: a + b, VectorOP.element_multiply(x, y), 0.0)


    def element_multiply(x, y):
        return list(map(lambda x_y: x_y[0] * x_y[1], zip(x, y)))


    def element_add(x, y):
        return list(map(lambda x_y: x_y[0] + x_y[1], zip(x, y)))


    def scala_multiply(v, s):
        return map(lambda e: e * s, v)


class Preceptron(object):

    # initialize the preceptron, set the number of parameters, the activate function
    def __init__(self, input_num, activator):
        self.activator = activator

        # initialize the weights to 0
        self.weights = [0.0] * input_num

        self.bias = 0.0


    # print the weights anf bias
    def __str__(self):
        return 'weights:\t%s\nbias:\t%f\n' % (self.weights, self.bias)


    # input the vector and predict the result]
    def predict(self, input_vec):
        # result = w1*x1 + w2*x2 + ... + wn*xn + w0, where w0 is the bias
        # use dot multiple to deal with the function
        return self.activator(VectorOP.dot(input_vec, self.weights) + self.bias)  # don't forget to put the result into the activator


    # training model
    def train(self, input_vec, labels, iteration, rate):
        for i in range(iteration):
            self._one_iteration(input_vec, labels, rate)


    # one training iteration
    def _one_iteration(self, input_vecs, labels, rate):
        # each training sample is like this: (input_vec, label)
        # pack all the samples into this form: [(input_vec1, label1), (input_vec2, label2), ...)
        samples = zip(input_vecs, labels)

        for (input_vec, label) in samples:
            output = self.predict(input_vec)
            self._update_weights(input_vec, output, label, rate)


    # update weights
    def _update_weights(self, input_vec, output, label, rate):
        # (1) calculate delta
        delta = label - output  # try here if delta = output - label
        self.weights = VectorOP.element_add(self.weights, VectorOP.scala_multiply(input_vec, rate * delta))
        self.bias += rate * delta


# get training data
def get_training_data():
    input_vecs = [[1, 1], [1, 0], [0, 1], [0, 0]]  # the truth table of and_ preceptron
    labels = [1, 0, 0, 0]  # the labels must correspond to the result of and operate
    return input_vecs, labels


# train the preceptron with and truth table
def train_perceptron():
    # creat a preceptron, the number pf parameter is 2, the activate function is f
    p = Preceptron(2, f)

    # training process
    input_vecs, labels = get_training_data()
    p.train(input_vecs, labels, 10, 0.1)

    # return the preceptron after trained
    return p


# define the activate function
def f(x):
    return 1 if x > 0 else 0


if __name__ == "__main__":
    # train the perceptron
    and_perceptron = train_perceptron()

    # print the weights of the model
    print(and_perceptron)

    # test the result
    print("1 and 1 = %d" % and_perceptron.predict([1, 1]))
    print("1 and 0 = %d" % and_perceptron.predict([1, 0]))
    print("0 and 1 = %d" % and_perceptron.predict([0, 1]))
    print("0 and 0 = %d" % and_perceptron.predict([0, 0]))