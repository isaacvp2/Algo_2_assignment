import sys

import input_parser

def main():
    try:
        lines = sys.stdin.readlines()

        k, m = input_parser.parse_input(lines)
        print(k)
        print(m)

    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
    


if __name__ == "__main__":
    main()