import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.asarray(X)
    Y = np.asarray(y)

    inv = np.linalg.inv(X.T @ X)
    return (inv @ X.T) @ Y