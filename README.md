# Programming Assignment 2: Greedy Algorithms

## Authors
* **Name 1:** Vinay Reddy Ratnam (UFID: 20765170)
* **Name 2:** Isaac Philipose (UFID: 86084445)

---

## Instructions to Compile/Build
Since this project is implemented in **Python 3**, there is no explicit compilation step (like `make` or `javac`). However, the environment must be set up correctly to run the scripts.

* **Prerequisites:** Python 3.6 or higher.
* **Dependencies:**
    * The read and write files (input_parser.py and output_writer.py) use only standard libraries (`sys`).

---

## Instructions to Run
The programs are designed to communicate via **Standard Input/Output (stdin/stdout)**. This allows for flexible testing and piping through main.py.

* **Basic Run (Output to Terminal):**
  ```bash
  python3 src/main.py < [Location of Input File]
  ```

* **Save Output to File:**
  ```bash
  python3 src/main.py < [Location of Input File] > [Name of Output File]
  ```

* **Example:**
  ```bash
  python3 src/main.py < data/input/input1.in > data/output/output1.out
  ```

## Assumptions

### Input Handling

* **Strict Formatting:** The input parser is strict. It expects exactly 2 non-empty lines. Blank lines in the middle will cause an error (to prevent parsing malformed data). The first line expects k (cache capacity) followed by a space and then m (the # of requests). Second line expects an m number of requests, each as an Integer ID and spaced out. Additionally, you cannot input negative numbers for m or k. However, you can include a variable number of spaces between each number on a line.


### Execution Environment

* It is assumed the user runs commands from the root of the repository (e.g., `python3 src/main.py` rather than `cd src; python3 main.py`).

---

## Written Component

### Question 1

| Input File | k | m | FIFO | LRU | OPTFF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| File1 | 5 | 100 | 49 | 52 | 33 |
| File2 | 20 | 200 | 70 | 68 | 40 |
| File3 | 3 | 50 | 19 | 18 | 12 |

OPTFF consistently has the least amount of misses for each input file
FIFO and LRU have a similar amount of misses for each input file

---

### Question 2


---

### Question 3

#### 1. 
