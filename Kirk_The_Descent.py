import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

mountain=[0,0,0,0,0,0,0,0]
# game loop
while 1:
    SX, SY = [int(i) for i in raw_input().split()]
    for i in xrange(8):
        MH = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        mountain[i]=MH
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    M = max(mountain)
    for j in xrange(8):
        if mountain[j] == M:
            X=j
    if SX == X:
        print "FIRE"
    else:
        print "HOLD" # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).