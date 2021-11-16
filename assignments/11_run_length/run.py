#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-11-10
Purpose: Run-length encoding/data compression
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str', metavar='str', help='DNA text or file')

    args = parser.parse_args()
    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()
    return args


# --------------------------------------------------
def run_length_encoding(seq):
    """define the run length encoding function"""
    compressed = []
    count = 1
    char = seq[0]
    for i in range(1, len(seq)):
        if seq[i] == char:
            count = count + 1
        else:
            compressed.append([char, count])
            char = seq[i]
            count = 1
    compressed.append([char, count])
    return compressed


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.str
    list = run_length_encoding(seq)
    compressed_seq = ''
    for i in range(0, len(list)):
        for j in list[i]:
            compressed_seq += str(j)
    string = compressed_seq.replace("1", "")
    print(string, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
