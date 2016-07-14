import sys

print "What is your name?"
name = raw_input() or sys.argv[1]
print "Hello %s!" % name

