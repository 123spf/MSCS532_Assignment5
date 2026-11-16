# Assignment 5: Quicksort Algorithm - Implementation, Analysis, and Randomization

## Overview

This repository contains the deliverables for Assignment 5. It explores the divide-and-conquer Quicksort algorithm by implementing both a Deterministic version and a Randomized version using the highly efficient **Hoare partition** scheme. 

By running the empirical testing script, you can observe firsthand how randomization shields the algorithm from its $O(n^2)$ worst-case time complexity vulnerabilities when confronted with sorted or reverse-sorted data.

## Repository Contents

*   `quicksort.py`: The main Python source code. It contains the logic for `quicksort_deterministic` and `quicksort_randomized`, alongside an empirical testing function that measures and prints execution times.
*   `Assignment5_Report.md`: A comprehensive analysis covering the time and space complexity, the theoretical decision-tree lower bounds of comparison sorting, and an evaluation of the empirical data.
*   `README.md`: Instructions for running the project.

## How to Run the Code

The implementation and the empirical testing suite are bundled into a single, easy-to-run Python script.

1.  Open your terminal or command prompt.
2.  Navigate to the directory containing the repository files.
3.  Execute the following command:
    `python3 quicksort.py`


## Summary of Findings

When you run the script, the program will generate an array of 1,000 integers and format it into three different distributions: Random, Sorted, and Reverse-Sorted. It will then sort these arrays using both algorithms and print the time it took.

**Key Observations:**
*   **Random Arrays:** Both the deterministic and randomized versions perform rapidly, completing the sort in a fraction of a millisecond. This represents the expected $O(n \log n)$ time complexity.
*   **Sorted and Reverse-Sorted Arrays:** The deterministic algorithm experiences a massive performance degradation, taking exponentially longer to sort the data. Because it always picks the first element as the pivot, the sorted data forces the partition to create extremely unbalanced splits, triggering the $O(n^2)$ worst-case scenario.
*   **The Power of Randomization:** The randomized algorithm maintains its lightning-fast $O(n \log n)$ speed across all distributions. By selecting the pivot randomly, it completely ignores the sorted layout of the data, proving that randomization is a highly effective way to guarantee efficient scaling.