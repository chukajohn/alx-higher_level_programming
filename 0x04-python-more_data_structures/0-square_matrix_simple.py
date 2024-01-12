#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matriz = []
    for line in maatrix:
        new_matriz.append([c**2 for c in line])
    return new_matriz
