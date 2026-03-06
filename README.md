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
For k = 3, there is a request sequence where OPTFF has less misses than LRU and FIFO
Sequence:
3 5
1 2 3 4 1

---

### Question 3
Prove OPTFF is Optimal
Let OPTFF be Belady’s Farthest-in-Future algorithm.

Let ( A ) be any offline algorithm that knows the full request sequence.

Prove that the number of misses of OPTFF is no larger than that of ( A ) on any fixed sequence.

Proof:

Suppose A and OPTFF start the beginning of a sequence the same but change at step i+1 when a new page causes a miss. To make space in the cache OPTFF evicts page p which is the furthest request, while algorithm A evicts a different page q.

With a new schedule A', that is the same A except it chooses to evict p instead of q at step i+1. Since page p is the page needed furthest, any later requests for q ust happen before the next request for p. If p or q is ever requested again A' will get a hit since it kept q in the cache while A will get a miss and has to evict a page to get back q.

If we make algorithm A evict page p at that specific time to fix the miss, the cache states of A and A' will be the same again. With this swap the new schedule A' matches OPTFF for an extra step without getting any extra misses compared to schedule A. By doing this exchange repeatedly for every step where the algorithms differ, we can change the algorithm A into OPTFF without increasing the miss count, proving that OPTFF is optimal.
#### 1. 
