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

    parser.add_argument('file',
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

    for fh in args.file:
        basename = os.path.basename(fh.name)
        root, ext = os.path.splitext(basename)
        seq_data = SeqIO.parse(fh, 'fasta')

    for i, rec in enumerate(seq_data,1):
        if i % 2 == 1:
           outdir = os.path.join(args.outdir, root + '_1' + ext)
        with open(outdir, 'wt') as fh:
           fh.write(">" + rec.description + "\n" + str(rec.seq) + "\n")
        if i % 2 == 0:
           outdir = os.path.join(args.outdir, root + '_2' + ext)
        with open(outdir, 'wt') as fh:
           fh.write(">" + rec.description + "\n" + str(rec.seq) + "\n")

    print(f'Done, see output in "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
