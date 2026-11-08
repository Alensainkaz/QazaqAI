import torch

x = torch.tensor(5.0, requires_grad=True)

y = x**2
y.backward()

print('Gradient', x.grad)
