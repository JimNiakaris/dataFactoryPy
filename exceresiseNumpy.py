import numpy as np

matrixA = np.random.randint(1,20,(4,5))
print(matrixA)
matrixB = np.add(matrixA,10)
print(matrixB)
matrixAT = np.transpose(matrixA)
print(matrixAT)

matrixDot = np.dot(matrixA,matrixAT)
print(matrixDot)

reshape1 = np.reshape(matrixA,(2,10))
print(reshape1)

reshape1 = np.reshape(matrixA,(1,20))
print(reshape1)

sortA = np.sort(matrixA)
print(sortA)

