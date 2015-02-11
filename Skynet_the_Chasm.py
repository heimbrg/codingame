import sys, math
J=0
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.
# game loop
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if S < G+1 and J==0:
        print "SPEED"
    elif X>R-2 and J==0:
        print "JUMP"
        J=1
    elif S > G+1 and J==0:
        print "SLOW"
    elif S>0 and J==1:
        print "SLOW"
    else:
        print "WAIT"