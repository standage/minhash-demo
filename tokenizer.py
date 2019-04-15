#!/usr/bin/env python3

import re

class Tokenizer(object):
    """Naive ngram tokenizer

    Some ideas stolen shamelessly from:
    http://www.albertauyeung.com/post/generating-ngrams-python/

    >>> text = 'It is our choices, Harry, that show what we truly are'
    >>> t1 = Tokenizer(text, n=35)
    >>> list(t1)
    ['ItisourchoicesHarrythatshowwhatwetr', 'tisourchoicesHarrythatshowwhatwetru', 'isourchoicesHarrythatshowwhatwetrul', 'sourchoicesHarrythatshowwhatwetruly', 'ourchoicesHarrythatshowwhatwetrulya', 'urchoicesHarrythatshowwhatwetrulyar', 'rchoicesHarrythatshowwhatwetrulyare']
    >>> t2 = Tokenizer(text, n=7, byword=True)
    >>> list(t2)
    ["('It', 'is', 'our', 'choices', 'Harry', 'that', 'show')", "('is', 'our', 'choices', 'Harry', 'that', 'show', 'what')", "('our', 'choices', 'Harry', 'that', 'show', 'what', 'we')", "('choices', 'Harry', 'that', 'show', 'what', 'we', 'truly')", "('Harry', 'that', 'show', 'what', 'we', 'truly', 'are')"]
    """
    def __init__(self, inputstr, n=5, byword=False):
        inputstr = re.sub(r'[^a-zA-Z0-9]', ' ', inputstr)  # convert non-alphanumeric chars to spaces
        inputstr = re.sub(r'\s+', ' ', str(inputstr))  # normalize whitespace
        self.input = inputstr
        self.byword = byword
        self.n = n

    def __iter__(self):
        if self.byword:
            tokens = [token for token in self.input.split(' ') if token != '']
        else:
            tokens = list(re.sub(r' ', '', self.input))
        for ngram in zip(*[tokens[i:] for i in range(self.n)]):
            if self.byword:
                ngram = repr(ngram)
            else:
                ngram = ''.join(ngram)
            yield ngram
