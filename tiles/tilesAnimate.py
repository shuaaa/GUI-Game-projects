#!/usr/local/bin/python
#
# tilesAnimate.py   - on ansi tt window, one frame per move
import sys, time
import tiles

def main () :
    lines = sys.stdin.readlines()
    game = None          # need to have board first
    for line in lines :
        line = line.strip()
        if line[0] == "(" :
            cost, move, board = eval(line)
            if not game : game = tiles.TileGame(board)
            future = cost-move
            mesg = "Move %d  - Future cost %d" % (move,future)
            sys.stdout.write('\033[1;1H\033[J') # clear screen
            game.printBoard(board,mesg)
            print "\f"
            time.sleep(1.0)   # wait between frames

if __name__ == "__main__" : main()
