#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-11-08
Purpose: Find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    seq = args.file.read()
    line = seq.splitlines()
    common = []
    line_num = len(line)
    if line_num < 3:
        base1 = line[0]
        base2 = line[1]
        for i in range(len(line[0])):
            if base1[i] == base2[i]:
                common.append("|")
            else:
                common.append("X")
    else:
        base1 = line[0]
        base2 = line[1]
        base3 = line[2]
        for i in range(len(line[0])):
            if base1[i] == base2[i] == base3[i]:
                common.append("|")
            else:
                common.append("X")
    print(seq, end="")
    print(''.join(common))


# --------------------------------------------------
if __name__ == '__main__':
    main()
