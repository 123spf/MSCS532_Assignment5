# Assignment 5: Quicksort Algorithm - Implementation, Analysis, and Randomization

## Overview

This repository contains the deliverables for Assignment 5. It explores the divide-and-conquer Quicksort algorithm by implementing both a Deterministic version and a Randomized version using the Hoare partition scheme.

By running the empirical testing script, you can observe how randomization protects the algorithm from its $O(n^2)$ worst-case time complexity vulnerabilities when sorting ordered or reverse-ordered data.

## Repository Contents

* `quicksort.py`: The main Python source code. It contains the logic for deterministic and randomized Quicksort using Hoare partitioning, along with an empirical testing suite that measures execution times across multiple input sizes and distributions.

* `assignment5.pdf`: A detailed report covering implementation choices, best/average/worst-case time and space complexity, the impact of randomization, and an evaluation of the empirical test results.

* `README.md`: Instructions for running the project and a summary of findings.

## How to Run the Code

The implementation and empirical tests are bundled into a single Python script.

1. Open your terminal or VS Code integrated terminal.
2. Navigate to the directory containing the repository files.
3. Execute the following command:
   `python3 quicksort.py`

## Summary of Findings

When executed, the script benchmarks both algorithms on array sizes of $n = 500$, $n = 1,000$, and $n = 2,000$ across three distributions: Random, Sorted, and Reverse-Sorted.

**Key Observations:**

* **Random Arrays:** Both the deterministic and randomized versions perform rapidly across all tested sizes (completing in roughly 0.5 to 4.5 milliseconds), reflecting expected $O(n \log n)$ scaling.
* **Sorted and Reverse-Sorted Arrays:** Deterministic Quicksort suffers severe quadratic $O(n^2)$ slowdowns as the input size grows (taking up to 0.153 seconds at $n = 2,000$) because selecting the first element consistently produces maximally unbalanced splits.
* **Impact of Randomization:** Randomized Quicksort maintains fast $O(n \log n)$ performance across all input distributions (finishing in roughly 3.0 to 4.4 milliseconds at $n = 2,000$), running up to 50 times faster than the deterministic version on sorted data.