from neuralnet import pre_active
import numpy as np
from torch import nn
import torch
# Create a simple neural net
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(3, 3)
        self.fc2 = nn.Linear(3, 1)
        nn.init.constant_(self.fc1.weight, 0.5)
        nn.init.constant_(self.fc1.bias, 0.5)
        nn.init.constant_(self.fc2.weight, 0.5)
        nn.init.constant_(self.fc2.bias, 0.5)
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        return x





def test_neuralnet():
    a = [4, 2, 3]
    w = [0.5, 1, 2]
    b = 0.5
    output = pre_active(a, w, b)
    assert output == 2
    a = [2, 1, 1]
    w = [0.25, 0.25, 0.25]
    b = 0.5
    output = pre_active(a, w, b)
    assert output == 1.5


    
    

    

