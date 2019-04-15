#!/usr/bin/env python3

from argparse import ArgumentParser
from sketch import MinHashSketch
from tokenizer import Tokenizer


cli = ArgumentParser()
cli.add_argument(
    '--by-word', action='store_true', help='tokenize ngrams by word; by '
    'default, ngrams are tokenized by character'
)
cli.add_argument(
    '-n', type=int, default=5, metavar='N', help='ngram size; default is 5'
)
cli.add_argument(
    '-s', '--size', type=int, default=20, metavar='S', help='MinHash sketch '
    'size; default is 20'
)
cli.add_argument('text1')
cli.add_argument('text2')
args = cli.parse_args()


with open(args.text1, 'r', encoding='utf-8') as fh:
    tok1 = Tokenizer(fh.read(), n=args.n, byword=args.by_word)
with open(args.text2, 'r', encoding='utf-8') as fh:
    tok2 = Tokenizer(fh.read(), n=args.n, byword=args.by_word)

mh1 = MinHashSketch(args.size)
mh1.consume_stream(tok1)
mh2 = MinHashSketch(args.size)
mh2.consume_stream(tok2)
dist = mh1.jacc_dist(mh2)
print('Jaccard distance:', round(dist, 4))
