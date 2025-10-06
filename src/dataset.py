# Daniel Hayes
# 10/5/25
# A chess move dataset object using torch library.

from torch.utils.data import Dataset

class ChessMoveDataset(Dataset):
    def __init__(self, tensors, labels):
        self.tensors = tensors
        self.labels = labels

    def __len__(self):
        return len(self.tensors)

    def __getitem__(self, idx):
        x = torch.tensor(self.tensors[idx], dtype=torch.float32)
        y = torch.tensor(self.labels[idx], dtype=torch.long)
        return x, y