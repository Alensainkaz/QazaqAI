import torch

x = torch.tensor([1.0, 2.0, 3.0])
target = torch.tensor([2.0, 4.0, 6.0])

w = torch.tensor(0.0,  requires_grad=True)

optimizer = torch.optim.SGD([w], lr=0.05)

for epoch in range(20):
    prediction = w * x
    loss = ((prediction - target)**2).mean()
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
    print(f'Epoch {epoch+1}: w = {w.item():.4f}, loss = {loss.item():.4f}')

