#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-09-27
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument(
        '-n',
        '--number',  # !!! identify the type
        help='Number the lines',
        action='store_true',
        default='False')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    for fh in args.files:
        for line_num, line in enumerate(fh, start=1):
            if args.number is True:
                print('     ' + f'{line_num}' + '\t' + f'{line}', end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
