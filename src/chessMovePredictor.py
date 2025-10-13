# Daniel Hayes
# 10/12/25

# Model class which inherets neural network module class.

import torch # type: ignore
import torch.nn as nn # type: ignore

class ChessMovePredictor(nn.Module):
    """
    This class uses torch neural network to analyze chess tensor positions - size 18x8x8.
    Initialized with the vocab size of all possible chess moves.
    """
    def __init__(self, vocab_size):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(18, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Flatten()
        )
        self.fc = nn.Sequential(
            nn.Linear(128 * 8 * 8, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, vocab_size)
        )

    def forward(self, x):
        return self.fc(self.conv(x))
