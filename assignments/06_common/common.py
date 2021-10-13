#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-10-12
Purpose: Find Common Words
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find Common Words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))
    parser.add_argument('FILE2',
                        metavar='FILE1',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    set1 = set(args.FILE1.read().split())
    set2 = set(args.FILE2.read().split())
    common = set1.intersection(set2)
    for word in common:
        if len(common) != 0:
            print(word, file=args.outfile)
        else:
            print(" There is no common word ")


# --------------------------------------------------
if __name__ == '__main__':
    main()
