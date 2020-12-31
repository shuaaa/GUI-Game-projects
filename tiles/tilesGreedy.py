#  tilesGreedy.py
#
#  Search for sequence of moves to bring a randomized tile puzzle
#  into order

from tiles import TileGame

def search(game, board) :
    path    = []
    closed  = {}         # boards already seen
    closed[board] = True # don't return (avoid loops)
    while True :
        path.append(board)
        if board == game.goal : break
        empty, moves = game.getMoves(board)
        candidates = []
        for mov in moves :
            child = game.makeMove(board,empty,mov)
            priority = game.futureCost(child)
            if not closed.get(child) :
                candidates.append( (priority,child) )
                closed[child] = True
        if candidates :
            candidates.sort()
            board = candidates[0][1]  # choose lowest cost board for next
        else :
            print "Cannot move from ",board
            break
    return path

def main() :
    import sys, time
    board = sys.argv[1]     # board is a 9 or 16 digit board
    game  = TileGame(board)

    startTime = time.time()
    path = search(game, board)
    endTime = time.time()-startTime

    print "tilesGreedy.py:",board,len(path),"moves"
    print "took", endTime, "secs"
    if len(path) < 99 : print path

if __name__ == "__main__" : main()
