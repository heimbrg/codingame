import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of points used to draw the surface of Mars.
for i in xrange(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    LAND_X, LAND_Y = [int(i) for i in raw_input().split()]

# game loop
j=0
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in raw_input().split()]
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    j += 1
    if VS < -20 and j>12:
        thrust=4
    elif j>12:
        thrust=3
    else:
        thrust=0
    print "0 %s" % thrust
    #print "-20 3" # R P. R is the desired rotation angle. P is the desired thrust power.
    