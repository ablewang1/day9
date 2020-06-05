import numpy as np
X1 = np.array([[1,2],[3,4]])
Y1 = np.array([[5,6],[7,8]])
X2 = np.array([[1,2,3],[1,2,3]])
Y2 = np.array([1,2,3])
## 数量积  使用np.dot
print(np.dot(X1,Y1))
print(np.dot(X2,Y2))
## 向量积  使用np.cross

print(np.cross(X1,Y1))
print(np.cross(X2,Y2))
## 普通乘积  使用np.multiply
print(np.multiply(X1,Y1)) #或者直接使用X1*Y1
print(np.multiply(X2,Y2)) #或者直接使用X2*Y2
