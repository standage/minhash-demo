# Demo of MinHash sketching for document comparison

```
$ ./test.py -n 5 -s 30 texts/text1.txt texts/text1.txt                                                 
Jaccard distance: 0.0
$ ./test.py -n 5 -s 30 texts/text1.txt texts/text1-a.txt                                               
Jaccard distance: 0.08
$ ./test.py -n 5 -s 30 texts/text1-a.txt texts/text1-b.txt                                             
Jaccard distance: 0.2222
$ ./test.py -n 5 -s 30 texts/text2.txt texts/text2.txt                                                 
Jaccard distance: 0.0
$ ./test.py -n 5 -s 30 texts/text2-a.txt texts/text2-b.txt                                             
Jaccard distance: 0.1034
$ ./test.py -n 3 --by-word -s 10 texts/text2-a.txt texts/text2-b.txt                                   
Jaccard distance: 0.1818
```

## A few notes

- This code is meant for demonstration purposes.
  I'm fairly confident the implementation of the MinHash sketch is correct (see notes below), but I didn't make any attempts at improving performance.
- This implementation relies on [Python's native `heapq` implementation of a heap queue (priority queue)](https://docs.python.org/3/library/heapq.html).
  Since this is optimized for removing the smallest item in the queue rather than the largest, this implementation is actually a top sketch (MaxHash sketch?) but should be mathematically equivalent to the canonical MinHash.
- If you want to adapt or use this code, you'll need to test/play around with/adjust the following.
    - sketch size: how many items will be stored in each MinHash sketch?
    - hash function: I use a simple MD5 hash of the string representation of each token.
      This is probably ok but there may be something better.
      In any case, you need a randomizing hash function: one that will hash the strings `gandalf`, `gandals`, and `sandals` to very different values.
    - tokenizer: I'm no expert in linguistics, so I make no guarantee that my text tokenizer is correct or even useful.
      I did the minimum amount of work needed to test the MinHash sketch.
