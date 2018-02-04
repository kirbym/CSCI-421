import sys
import library as c

if len(sys.argv) <= 1:
    print "I need a key!"
    sys.exit(1)

key = int(sys.argv[1])
text = ""

if len(sys.argv) == 2:
    #only key, get input from 'cin'
    text = sys.stdin.read()
else:
    #file = open(sys.argv[2])
    #text = file.read('R')
    #file.close()
    with open(sys.argv[2]) as file:
        text = file.read()
        #with is safer way of doing the above commented code

print

c.caesar(text, (26 - key))

print