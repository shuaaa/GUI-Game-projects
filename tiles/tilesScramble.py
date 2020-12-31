#  tilesScramble.py
#
#  Scramble the solution by making N random moves.

def scramble(dim, times) :
    import tiles, random

    game = tiles.TileGame(dim=dim)
    board = game.goal                  # start with solution
    used = {board: True}               # mark it "taken"
    while times > 0 :
        used[board] = True
        empty, moves = game.getMoves(board)
        move = random.choice(moves)
        nextBoard = game.makeMove(board,empty,move)
        if used.get(nextBoard) : continue
        board = nextBoard
        times -= 1
    return board

def main() :
    import sys
    dim   = int(sys.argv[1])   # 3 or 4 for the size of board
    moves = int(sys.argv[2])   # Number of times to randomly move
    print scramble(dim, moves)

if __name__ == "__main__" : main()
