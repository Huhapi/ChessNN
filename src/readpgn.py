# Daniel Hayes
# 10/5/25
# Reading games from PGN file.
import chess.pgn # type: ignore
import lowpieces as lp

def get_data():
    """
    Get data retrieves the chess games from the pgn file.
    output: A touple of lists of lists- games of moves in uci format.
    A list of the games via a list of moves
    A list of the games via lists of fen board positions - with perfect play via syzygy tablebase with less than 5 pieces.
    """
    gamepositions = []
    games = []
    
    pgn_file = f"src\chess_games\chess_com_games_2025-10-04.pgn"
    file_game_count = 0

    try:
        with open(pgn_file) as f:
            while True:
                game = chess.pgn.read_game(f)
                if game is None:
                    break

                board = game.board()
                positions = []
                moves = []

                for move in game.mainline_moves():
                    fen = board.fen()

                    if len(board.piece_map()) <= 5:
                        # Switch to tablebase perfect play
                        playdtz = True
                        while playdtz:
                            best = lp.endgame_move(board.fen())
                            if not best:
                                playdtz = False  # No move found
                            else:
                                
                                if(board.is_game_over()):
                                    break
                                moves.append(best.uci())
                                positions.append(board.fen())
                                board.push(best)
                                

                        break  # Stop parsing original PGN, tablebase used instead.
                    else:
                        moves.append(move.uci())
                        positions.append(fen)
                        board.push(move)

                if moves:
                    games.append(moves)
                    gamepositions.append(positions)
                    file_game_count += 1

        print(f"File done. Games added: {file_game_count}. Total games so far: {len(games)}")

    except FileNotFoundError:
        print(f"File not found. Skipping.")

    return games,gamepositions