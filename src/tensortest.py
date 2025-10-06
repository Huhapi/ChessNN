# Daniel Hayes
# 10/5/25
# Tensor test
import numpy as np
import tensor
import readpgn
import chess
import dataset

def test_empty_board():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    tensit = tensor.fen_to_tensor(fen)

    # Check shape
    print("Tensor shape:", tensit.shape)

    # Check piece planes
    print("White pawns (channel 0):")
    print(tensit[0])

    print("Black knights (channel 7):")
    print(tensit[7])

    # Check side to move
    print("Side to move (channel 12):")
    print(tensit[12][0][0])  # Should be 1 for white

    # Check castling rights
    print("White kingside castling (channel 13):", tensit[13][0][0])  # Should be 1
    print("Black queenside castling (channel 16):", tensit[16][0][0])  # Should be 1

    # Check en passant (should be all zeros)
    print("En passant (channel 17):", np.sum(tensit[17]))  # Should be 0

    # Check move count
    print("Move count (channel 18):", tensit[18][0][0])  # Should be 0.01

def tensor_run_test():
    gamemoves,gamepositions = readpgn.get_data()

    tensors = []
    moves = []
    for game in range(len(gamepositions)):
        for move in range(len(gamepositions[game])):
            tensors.append(tensor.fen_to_tensor(gamepositions[game][move]))
            moves.append(gamemoves[game][move])
            
    data = dataset.ChessMoveDataset(tensors,moves)
    print(len(moves),len(tensors))
    return data


def main():
    #test_empty_board()
    data = tensor_run_test()
    

main()