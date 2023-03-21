import torch
from torch import nn

x=torch.tensor([1.])
model = nn.Linear(1,1) # layer : input node one, output node one

print('weights : ', model.weight) # initialize
print('bias : ', model.bias)

y = model(x)
print(y) # y = wx + b

y = x @ model.weight + model.bias
print(y)

###########################################
fc1 = nn.Linear(1,3) # fully-connected (FC)
fc2 = nn.Linear(3,1)

print('FC_1 weights : ', fc1.weight)
print('FC_1 bias : ', fc1.bias)
print('FC_2 weights : ', fc2.weight)
print('FC_2 bias : ', fc2.bias)

x=torch.tensor([1.])
x=fc1(x)
print('FC_1 output : ', x)
x=fc2(x)
print('FC_2 output : ',x)

x=torch.tensor([1.])
y = (x@fc1.weight.T+fc1.bias)@fc2.weight.T+fc2.bias
print(y)

###########################################
fc1 = nn.Linear(1,3)
fc2 = nn.Linear(3,1)

x=torch.tensor([1.])
x=fc1(x)
print(x)
x=fc2(x)
print(x)

model = nn.Sequential(fc1, fc2) # Sequential layer 
x=torch.tensor([1.])
print(model(x))


model = nn.Sequential(nn.Linear(2,5), # channel x channel
                      nn.Linear(5,10),
                      nn.Linear(10,3))
x=torch.randn(2)
print(x)
print(model(x))

x=torch.randn(1,2)
print(x)
print(model(x))

x=torch.randn(5,2) # data x channel => 5 datasets with 2 channel(height and weight)
print(x)
print(model(x))

x=torch.randn(2,3,1,4,5,2)
print(model(x).shape)