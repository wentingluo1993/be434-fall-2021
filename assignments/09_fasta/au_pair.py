#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-10-27
Purpose: Split interleaved/paired reads
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        metavar='DIR',
                        help='Output directory',
                        type=str,
                        default='split')

    args = parser.parse_args()
    if not os.path.isdir(args.outdir):
        os.mkdir(args.outdir)

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    out_dir = args.outdir

    for fh in args.files:
        root, ext = os.path.splitext(os.path.basename(fh.name))
        forward = open(os.path.join(out_dir, root + '_1' + ext), "wt",encoding='utf-8')
        reverse = open(os.path.join(out_dir, root + '_2' + ext), "wt",encoding='utf-8')
        parser = SeqIO.parse(fh, 'fasta')
        for i, rec in enumerate(parser):
            SeqIO.write(rec, forward if i % 2 == 0 else reverse, 'fasta')
    print(f'Done, see output in "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
