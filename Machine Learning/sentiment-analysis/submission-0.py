import torch
import torch.nn as nn
from torchtyping import TensorType

class Solution(nn.Module):
    def __init__(self, vocabulary_size: int):
        super().__init__()
        torch.manual_seed(0)
        self.embedding_layer = nn.Embedding(vocabulary_size, 16)
        self.linear_layer = nn.Linear(16, 1)
        self.sigmoid_layer = nn.Sigmoid()


    def forward(self, x: TensorType[int]) -> TensorType[float]:
        out = self.embedding_layer(x)
        out = torch.mean(out, axis = 1)
        out = self.sigmoid_layer(self.linear_layer(out))
        return out