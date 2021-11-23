#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-11-22
Purpose: Python grep
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python grep',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for fh in args.files:
        for line in fh:
            condition1 = re.search(args.pattern, line, re.I)
            condition2 = re.search(args.pattern, line)
            if args.insensitive:
                if (condition1) and (len(args.files) > 1):
                    print(f'{fh.name}:{line}', file=args.outfile, end="")
                if (condition1) and (len(args.files) == 1):
                    print(line, file=args.outfile, end="")
            else:
                if (condition2) and (len(args.files) > 1):
                    print(f'{fh.name}:{line}', file=args.outfile, end="")
                if (condition2) and (len(args.files) == 1):
                    print(line, file=args.outfile, end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
