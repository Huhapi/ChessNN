# Daniel Hayes
# 10/10/25

# Testing the end game database
import lowpieces as lp

def test_kq():
    """ Test a king and queen position end game. """
    fen = "8/8/8/6Q1/8/8/5K1k/8 w - - 0 1"
    move = lp.endgame_move(fen)
    
    print(move)

def test_kr():
    """ Test a king and rook position end game. """
    fen = "8/8/8/6R1/8/8/5K2/7k b - - 0 1"
    move = lp.endgame_move(fen)

    print(move)

def main():
    test_kr()




main()