import torch

target = torch.tensor(10.0)

prediction = torch.tensor(7.0)

loss = (target-prediction)**2

print("Target:", target)
print("Prediction:", prediction)
print("Loss:", loss)