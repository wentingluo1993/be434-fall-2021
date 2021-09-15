#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-09-14
Purpose: sum numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='sum numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Positional arg
    parser.add_argument('int', metavar='INT', type=int, nargs='+',
                        help='Numbers to add')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    int_arg = args.int  # .int should be the same with line 20

    int_arg_string = map(str,int_arg)
    print(' + '.join(int_arg_string) +  ' = '  + str(sum(int_arg)) )


# --------------------------------------------------
if __name__ == '__main__':
    main()

