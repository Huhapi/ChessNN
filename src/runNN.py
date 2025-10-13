# Daniel Hayes
# 10/5/25
# This is the controls of the chess learning program.
# It uses the functions from support library files and the chess games to learn chess.
# Mainly torch, and tensors
import readpgn
import tensor
import dataset
import move_set 
import torch # type: ignore
import torch.cuda # type: ignore
from torch.utils.data import Dataset, DataLoader # type: ignore
import torch.nn as nn # type: ignore
import chessMovePredictor

gamemoves,gamepositions = readpgn.get_data()

tensors = []
moves = []
for game in range(len(gamepositions)):
    for move in range(len(gamepositions[game])):
        tensors.append(tensor.fen_to_tensor(gamepositions[game][move]))
        moves.append(gamemoves[game][move])

# Load the uci move vocabulary
uci_to_index = move_set.generate_full_uci_vocab()

# data is the ChessMoveDataset object, being fed the list of tensors and list of uci moves
data = dataset.ChessMoveDataset(tensors,moves,uci_to_index)
# Using torch DataLoader object
dataloader = DataLoader(data, batch_size=64, shuffle=True)



# Setting up device, model, optimizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = chessMovePredictor.ChessMovePredictor(vocab_size=len(uci_to_index)).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

for epoch in range(6):  # epoch is the number of iterations we use to train our data.
    total_loss = 0
    for x_batch, y_batch in dataloader:
        x_batch, y_batch = x_batch.to(device), y_batch.to(device)

        logits = model(x_batch)
        loss = loss_fn(logits, y_batch)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1} | Loss: {total_loss/len(x_batch):.4f}")

torch.save(model.state_dict(), "src/results/model_weights.pth")

