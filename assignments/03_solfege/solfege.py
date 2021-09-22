#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-09-20
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Solfege', nargs='+')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    jumper = {'Do': 'Do, A deer, a female deer',
              'Re': 'Re, A drop of golden sun',
              'Mi': 'Mi, A name I call myself',
              'Fa': 'Fa, A long long way to run',
              'Sol': 'Sol, A needle pulling thread',
              'La': 'La, A note to follow sol',
              'Ti': 'Ti, A drink with jam and bread'}

    for char in args.text:
        print(jumper.get(char, 'I don\'t know "{}"'.format(char)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
