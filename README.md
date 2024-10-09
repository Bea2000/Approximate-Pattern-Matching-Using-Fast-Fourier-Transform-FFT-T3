# Approximate Pattern Matching Using Fast Fourier Transform (FFT)

## Project Overview

This project is part of the **Design and Analysis of Algorithms** course taken in the second semester of 2023 at **Pontificia Universidad Católica de Chile**. The goal of the project is to detect approximate pattern matches between a string `T` of length `M` and a string `S` of length `N`, given a relaxation level `K`, using Fast Fourier Transform (FFT) for efficient computation.

## Problem Statement

We aim to find the number of approximate matches of string `T` within string `S`, where an approximate match at position `i` allows for up to `K` deviations in the matching position for each character. Specifically, for each position `j` in `T`, there should exist a position `z` in `S` such that `|z - j| ≤ K` and `T[j] == S[z]`. 

For example, for `T = "ABC"` and `S = "ABBCBA"`, with `K = 1`, there are two approximate matches at positions `1` and `2`.

### Input

The input consists of:
1. Three integers `N`, `M`, and `K` (`1 ≤ M ≤ N ≤ 5000`, `0 ≤ K ≤ 5000`), representing the lengths of the strings and the allowed relaxation level.
2. A string `S` of length `N` containing only the characters `A`, `B`, and `C`.
3. A string `T` of length `M` containing only the characters `A`, `B`, and `C`.

### Output

The output is a single integer representing the number of approximate matches of `T` in `S`.

### Example

#### Input

```plaintext
10 2 0 BCBCBBCCAA CB
```

#### Output

```plaintext
2
```


## Objectives

1. **Optimize pattern matching** using FFT to reduce the time complexity to `O(N log N)`.
2. **Handle approximate matches** by incorporating relaxation up to `K` positions for each character in `T`.
3. **Ensure efficiency** to meet the 3-second execution time constraint for all input cases.

## Requirements

- Python 3.x
- Libraries: `cmath`, `math`

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
    ```

2. Run the script:

   ```bash
   python3 main.py < tests/input/input_xx.txt
   ```

## Expected Complexity

The expected time complexity for the solution is **O(N log N)** due to the use of FFT for polynomial multiplication, which efficiently computes convolutions.