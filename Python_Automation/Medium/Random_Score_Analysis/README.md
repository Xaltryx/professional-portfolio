# Random_Score_Analysis

A testing script generates random quality scores for incoming products, then analyzes them using built-in functions.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Data](#sample-data)
* [Sample Input/Output](#sample-inputoutput)
* [Learning Objective](#learning-objective)
* [Allowed Libraries](#allowed-libraries)
* [Task Type](#task-type)

## Problem Statement

Create a function `generate_scores(n)` that returns a list containing `n` random integers between **1 and 10** using `random.randint()`.
Then write another function `analyze(scores)` that prints:

* highest score (using `max()`)
* lowest score (using `min()`)
* number of scores (using `len()`)

Handle the edge case where `n` is **0**: in that case, print **"No scores to analyze"**.

## Sample Data

Normal case: `n = 10`
Edge case: `n = 0`

## Sample Input/Output

**Normal Example:**

```python
Input: n = 5
scores: [4, 7, 1, 10, 6]
max: 10
min: 1
count: 5
```

**Edge Case:**

```python
Input: n = 0
No scores to analyze
```

## Learning Objective

Practice defining and calling functions, using the `random` module, list operations, and built-in functions (`max`, `min`, `len`).

## Allowed Libraries

random

## Task Type

Data structure + function + computation + validation
