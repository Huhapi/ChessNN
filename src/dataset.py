# Daniel Hayes
# 10/5/25
# A chess move dataset object using torch library.
import torch # type: ignore
from torch.utils.data import Dataset # type: ignore

class ChessMoveDataset(Dataset):
    def __init__(self, tensors, labels, uci_to_index):
        self.tensors = tensors
        self.moves = labels
        self.uci_to_index = uci_to_index

    def __len__(self):
        return len(self.moves)

    def __getitem__(self, idx):
        x = self.tensors[idx]
        y = self.uci_to_index[self.moves[idx]]
        return torch.tensor(x), torch.tensor(y)