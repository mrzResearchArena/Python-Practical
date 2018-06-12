
def matrixMultiplication(x, y):
    assert x.shape[1] == y.shape[0], 'Check matrix dimension'

    x = x.copy()
    y = y.copy()

    result = np.empty(shape=(x.shape[0], y.shape[1]))

    for row in range(x.shape[0]):
        for column in range(y.shape[1]):
            result[row, column] = np.sum(x[row,:] * y[:,column])

    return result

print(matrixMultiplication(x, y))
