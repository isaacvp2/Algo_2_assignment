import sys

import input_parser
import fifo
import lru
import optff
import output_writer

def main():
    try:
        lines = sys.stdin.readlines()

        k, m = input_parser.parse_input(lines)

        fifo_misses = fifo.fifo(k, m)
        lru_misses = lru.lru(k, m)
        optff_misses = optff.optff(k, m)

        output_writer.write_output(fifo_misses, lru_misses, optff_misses)


    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
    


if __name__ == "__main__":
    main()