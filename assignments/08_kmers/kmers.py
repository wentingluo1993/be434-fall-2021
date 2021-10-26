#!/usr/bin/env python3
"""
Author : wenting <wenting@localhost>
Date   : 2021-10-25
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=argparse.FileType('rt'))
    parser.add_argument('file2',
                        metavar='FILE1',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='K-mer size',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()
    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')
    return args


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def count_kmers(file, k):
    """ Count kmers and restore kmers to dictionaries """
    words = {}
    for line in file:
        for word in line.split():
            for kmer in find_kmers(word, k):
                if kmer not in words:
                    words[kmer] = 1
                # increment the count of this "kmer" in "words1"
                else:
                    words[kmer] += 1
    return words


# --------------------------------------------------
def main():
    """ Find the common kmers between the two input files """
    args = get_args()
    file1 = args.file1.read().split()
    file2 = args.file2.read().split()
    words1 = count_kmers(file1, args.kmer)
    words2 = count_kmers(file2, args.kmer)
    common = set(words1).intersection(set(words2))
    for word in common:
        if len(common) != 0:
            print(f'{word:10} {words1.get(word):5} {words2.get(word):5}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
