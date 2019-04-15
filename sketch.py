#!/usr/bin/env python3

import hashlib
import heapq


def myhash(value):
    return hashlib.md5(value.encode('utf-8')).digest()


class MinHashSketch(object):
    def __init__(self, size, initlist=list(), hashfunc=myhash):
        assert size > 0
        self.hashfunc = hashfunc
        self.size = size
        self.queue = list(initlist)  # Copy the list so original remains unchanged
        heapq.heapify(self.queue)

    def consume(self, value, skiphash=False):
        if not skiphash:
            value = self.hashfunc(value)
        heapq.heappush(self.queue, value)
        if len(self.queue) > self.size:
            heapq.heappop(self.queue)

    def consume_stream(self, stream, skiphash=False):
        for value in stream:
            self.consume(value, skiphash=skiphash)

    def jacc_coef(self, other):
        A = set(self.queue)
        B = set(other.queue)
        return len(A.intersection(B)) / len(A.union(B))

    def jacc_dist(self, other):
        return 1.0 - self.jacc_coef(other)
