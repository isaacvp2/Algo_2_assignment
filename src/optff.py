def optff(k, m):
    cache = set()
    misses = 0

    for index, l in enumerate(m):
        if l not in cache:
            misses += 1
              
            if len(cache) == k:
                element_to_dist = {}

                for req in range(len(m) - 1, index, -1):
                    if m[req] in cache:
                        element_to_dist[m[req]] = req
                
                element_to_evict = None
                
                for item in cache:
                    if item not in element_to_dist:
                        element_to_evict = item
                        break
                
                if element_to_evict is None:
                    element_to_evict = max(element_to_dist, key=element_to_dist.get)
                
                cache.remove(element_to_evict)
            
            cache.add(l)

    return misses