# Daniel Hayes
# 10/5/25
# Reading games from PGN file.
import chess.pgn


def get_data():
    """
    Get data retrieves the chess games from the pgn file.
    output: A touple of lists of lists.
    A list of the games via a list of moves
    A list of the games via lists of fen board positions.
    """
    gamepositions = []
    games = []

    #for a in range(1, 40):
    pgn_file = f"chess_games/chess_com_games_2025-10-04.pgn"
    file_game_count = 0

    try:
        with open(pgn_file, encoding="utf-8") as f:
            while True:
                game = chess.pgn.read_game(f)
                if game is None:
                    break

                board = game.board()
                positions = []
                moves = []

                for move in game.mainline_moves():
                    positions.append(board.fen())
                    moves.append(move.uci())
                    board.push(move)

                if moves:
                    games.append(moves)
                    gamepositions.append(positions)
                    file_game_count += 1

        print(f"File done. Games added: {file_game_count}. Total games so far: {len(games)}")

    except FileNotFoundError:
        print(f"File not found. Skipping.")

    return games,gamepositions