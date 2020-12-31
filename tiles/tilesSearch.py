#  tilesSearch.py
#
#  Search for sequence of moves to bring a randomized tile puzzle
#  into order

import time, Queue
from   tiles  import TileGame

def main() :
    import sys, re
    ratio = int(sys.argv[1]) # future to past cost
    board = sys.argv[2]
    game  = TileGame(board)
    startTime = time.time()
    path = search(game,board,ratio)
    endTime = time.time()-startTime
    print "tilesSearch.py: Move=", len(path), "Search took", endTime, "secs"
    for entry in path : print entry

def search(game, board, ratio) :
    closed  = {}
    queue   = Queue.PriorityQueue()
    origCost = game.futureCost(board)*ratio
    orig = (origCost,0,board,None) # (cost,nMoves,board,parent)
    queue.put(orig)
    closed[orig] = True
    expanded = 0
    solution = None
    while queue and not solution :
        parent = queue.get()  
        expanded += 1
        (parCost, parMoves, parBoard, ancester) = parent
        empty, moves = game.getMoves(parBoard)
        for mov in moves :
            childBoard = game.makeMove(parBoard,empty,mov)
            if closed.get(childBoard) : continue
            closed[childBoard] = True
            childMoves = parMoves+1
            childCost = game.futureCost(childBoard)*ratio + childMoves
            child = (childCost,childMoves,childBoard,parent)
            queue.put(child)
            if childBoard == game.goal : solution = child

    if solution :
        print expanded, "entries expanded. Queue still has " , queue.qsize()
        # find the path leading to this solution
        path = []
        while solution :
            path.append(solution[0:3]) # drop the parent
            solution = solution[3]     # to grandparent
        path.reverse()
        return path
    else :
        return []

if __name__ == "__main__" : main()
