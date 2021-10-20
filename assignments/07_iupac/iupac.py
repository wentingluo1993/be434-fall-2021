#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-10-18
Purpose: Expand IUPAC codes
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

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
    IUPAC_table = {
        'A': 'A',
        'C': 'C',
        'G': 'G',
        'T': 'T',
        'U': 'U',
        'M': '[AC]',
        'R': '[AG]',
        'W': '[AT]',
        'S': '[GC]',
        'Y': '[CT]',
        'K': '[GT]',
        'V': '[ACG]',
        'H': '[ACT]',
        'D': '[AGT]',
        'B': '[CGT]',
        'X': '[ACGT]',
        'N': '[ACGT]'
    }

    for seq in args.seq:
        regular = ''
        for char in seq:
            regular = regular + IUPAC_table.get(char, '-')
        if args.outfile is not sys.stdout:
            print('{} {}'.format(seq, regular), file=args.outfile)
        else:
            print('{} {}'.format(seq, regular))
    if args.outfile is not sys.stdout:
        print('Done, see output in "{}"'.format(args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
