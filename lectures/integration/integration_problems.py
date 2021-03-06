import numpy as np


def problem_smooth(x):
    return np.exp(-x)


def problem_kinked(x):
    return np.sqrt(np.abs(x))


def problem_genz_discontinuous(x, u=np.array([0.5, 0.5]), a=np.array([5, 5])):
    if x[0] > u[0] or x[1] > u[1]:
        return 0
    else:
        return np.exp((a * x).sum())
