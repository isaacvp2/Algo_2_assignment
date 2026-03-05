import sys

def write_output(fifo_misses, lru_misses, optff_misses):
    sys.stdout.write(f'FIFO  : {fifo_misses}\n')
    sys.stdout.write(f'LRU   : {lru_misses}\n')
    sys.stdout.write(f'OPTFF : {optff_misses}\n')
