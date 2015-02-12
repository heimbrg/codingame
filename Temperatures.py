import sys, math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
Ta=[]
N = int(raw_input()) # the number of temperatures to analyse
if N ==0:
    print 0
else:
    TEMPS = raw_input() # the N temperatures expressed as integers ranging from -273 to 5526

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    TEMPS = [int(s) for s in TEMPS.split(' ')]
    for i in range(0,len(TEMPS)):
        Ta.append(abs(TEMPS[i]))
    x = min(Ta)
    print x