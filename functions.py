import numpy as np


def rotate_180(mat):
    mat = np.rot90(mat)
    mat = np.rot90(mat)
    return mat
    

def rotate_270(mat):
    mat = np.rot90(mat)
    mat = np.rot90(mat)
    mat = np.rot90(mat)
    return mat