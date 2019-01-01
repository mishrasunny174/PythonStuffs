#!/usr/bin/env python
import sys

def gcd(a,b):
	while a%b != 0:
		a,b = b, a%b
	return b	

def main():
	if len(sys.argv) != 3:
		print "Usage: %s num1 num2" % sys.argv[0]
	else:
		print "GCD: %d" % gcd(int(sys.argv[1]),int(sys.argv[2]))

if __name__ == "__main__":
	main()