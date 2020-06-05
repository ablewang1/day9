import torch
import numpy as np

a = torch.Tensor([[4,0,3],[-5,9,-23]])
b = a.numpy()
print(np.linalg.norm(b,ord=np.inf,axis=0)) #无穷范数
print(np.linalg.norm(b,ord=np.inf,axis=1)) #无穷范数

print(np.linalg.norm(b,ord=1,axis=1)) #一范数
print(np.linalg.norm(b,ord=2,axis=0)) #二范数

print(np.linalg.norm(b,ord=0,axis=0)) #零范数