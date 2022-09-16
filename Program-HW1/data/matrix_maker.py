#!/usr/bin/env python

"""Create random integer n×n matrices."""

# Core Library modules
import random

random.seed(1234)

def create_random_matrix(n):
    #max_val = 1000  # I don't want to get Java / C++ into trouble ;-)
    matrix = []
    for i in range(n):
        matrix.append([random.randint(0, max_val) for el in range(n)])
    return matrix


def save_matrix(A, B, filename):
    f = open(filename, "w")
    for i, matrix in enumerate([A, B]):
        if i != 0:
            f.write("\n")
        for line in matrix:
            f.write("\t".join(map(str, line)) + "\n")