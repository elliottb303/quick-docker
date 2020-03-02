#!/usr/bin/env python
import sys
import ast

# sort two arrays of integers input as args
def main():
    if len (sys.argv) < 3:
        print('Number of input arguments:', len(sys.argv), 'arguments.')
        print("Expeected 2 lists input.")
        return 1
    if type(sys.argv[1]) != str or type(sys.argv[2]) != str or len(sys.argv[1] + sys.argv[2]) > 56:
        print("Expected a small list of integers as args")
        return 1
    print(sorted(ast.literal_eval(sys.argv[1]) + ast.literal_eval(sys.argv[2])))

if __name__ == "__main__":
    main()
