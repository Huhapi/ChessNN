# Daniel Hayes
# 10/12/25

# This takes the saved model, loads it, and lets you play against it using pygames.
import torch # type: ignore
import chessMovePredictor as m # type: ignore
import tensor as t
import move_set as ms
import chess # type: ignore

class retrieveMove():
    def __init__(self):
        self.move_to_uci = ms.generate_full_uci_vocab()
        self.uci_to_move = self.get_ruci()

    def get_ruci(self):
        inv_vocab = {v: k for k, v in self.move_to_uci.items()}
        return inv_vocab
    
    def getmove(self, fen):
        """
        This function takes in a fen representation of a chess board, uses it to retrieve
        the move predicted by the torch neural network. It returns the best fitting legal move.
        If there are none, it returns a random legal move.

        Args: chess board fen

        returns: move in uci format
        """
        # initializing torch model
        model = m.ChessMovePredictor(len(self.uci_to_move))  
        model.load_state_dict(torch.load("src/results/model_weights.pth"))
        model.eval()  # switch to inference mode

        board = chess.Board(fen)
        legal_uci = []
        for move in board.legal_moves:
            legal_uci.append(move.uci())
        itensor = t.fen_to_tensor(fen)
        input_tensor = torch.tensor(itensor, dtype=torch.float32).unsqueeze(0)
        
        move = None
        with torch.no_grad():
            logits = model(input_tensor)  # shape: (1, vocab_size)

            topk_indices = torch.topk(logits, k=10).indices[0].tolist() # Grabs the top 10 predicted moves

            for idx in topk_indices:
                move_uci = self.uci_to_move[idx]

                # Looking for moves in legal moves
                if move_uci in legal_uci:
                    return move_uci
            if board.legal_moves:
                legal_moves = list(board.generate_legal_moves())
                return legal_moves[0].to_uci()
            else:
                return None