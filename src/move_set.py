# Daniel Hayes
# 10/6/25

import chess # type: ignore

def generate_full_uci_vocab():
    move_set = {}
    x = 0
    for from_square in chess.SQUARES:
        for to_square in chess.SQUARES:
            move = chess.Move(from_square, to_square)
            move_set[move.uci()] = x
            x += 1
            # Add promotions if moving to rank 8 from rank 7 (white) or rank 1 from rank 2 (black)
            from_rank = chess.square_rank(from_square)
            to_rank = chess.square_rank(to_square)

            if (from_rank == 6 and to_rank == 7) or (from_rank == 1 and to_rank == 0):
                for promo in [chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT]:
                    move = chess.Move(from_square, to_square, promotion=promo)
                    move_set[move.uci()] = x
                    x += 1

    #uci_to_index = {uci: i for i, uci in enumerate(move_set)}
    #index_to_uci = {i: uci for i, uci in enumerate(move_set)}

    return move_set