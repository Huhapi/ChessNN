# Daniel Hayes
# 10/5/25
# Tensor test
import numpy as np
import tensor
import readpgn
import chess
import dataset
import move_set

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

def test_move_set():
    y = move_set.generate_full_uci_vocab()
    print(y)
    print(len(y))

def validate_moves():

    all_moves, x = readpgn.get_data()
    uci_to_index = move_set.generate_full_uci_vocab()
    flat_moves = [move for game in all_moves for move in game]
    missing = set()

    for move in flat_moves:
        if move not in uci_to_index:
            missing.add(move)

    if missing:
        print(f"❌ {len(missing)} moves not found in vocabulary:")
        for m in sorted(missing):
            print(m)
    else:
        print("✅ All dataset moves are covered by the vocabulary.")


def test_pgnreader():
    all_moves, x = readpgn.get_data()
    size = 0
    posize = 0
    for game in all_moves:
        size += len(game)
    for pos in x:
        posize += len(pos)
    print("moves: ",size,", positions: ",posize)


def main():
    #test_empty_board()
    #data = tensor_run_test()
    test_move_set()
    #validate_moves()
    #test_pgnreader()

main()