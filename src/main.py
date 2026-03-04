import sys

def fifo(k, m):
    cache = set()
    queue = []
    misses = 0

    for l in m:
        if l not in cache:
            misses += 1
            if len(cache) == k:
                deleted = queue.pop(0)
                cache.remove(deleted)
            cache.add(l)
            queue.append(l)
    return misses
