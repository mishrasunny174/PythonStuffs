#!/usr/bin/env python

import binascii
import sys

def decode(str):
	return binascii.unhexlify(str)

def main():
	if len(sys.argv) != 3:
		print("Usage: %s <input file name> <output file name>\n" % sys.argv[0])
		exit()
	try:
		inputFile = open(sys.argv[1],'r')
		outputFile = open(sys.argv[2],'wb')
		inputData = inputFile.read()
		outputData = decode(inputData)
		outputFile.write(outputData)
		inputFile.close()
		outputFile.close()
	except Exception as e:
		print("ERROR: s" % e.message)

if __name__ == "__main__":
	main()