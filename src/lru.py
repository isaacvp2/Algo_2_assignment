def lru(k, m):
    cache = {}
    misses = 0

    for l in m:
        if l in cache:
            del cache[l]
            cache[l] = True
        else: 
            misses += 1
            if len(cache) == k:
                deleted = next(iter(cache))
                del cache[deleted]
            cache[l] = True
    return misses