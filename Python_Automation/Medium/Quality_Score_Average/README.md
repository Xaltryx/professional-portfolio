# Quality_Score_Average

A production inspector enters quality scores (1–10). Typing **-1** stops data entry.
Negative values (except -1) should be skipped.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Input/Output](#sample-inputoutput)
* [Learning Objective](#learning-objective)
* [Task Type](#task-type)

## Problem Statement

Create a program that repeatedly asks the user for integer scores until they enter **-1**.
Use **continue** to skip any negative value except -1, and **break** to stop the loop when -1 is typed.
After finishing input, compute and print the average score. If no valid scores were entered, print
**"No valid scores to average."**

## Sample Input/Output

### Normal Case

```python
Enter score: 8
Enter score: 10
Enter score: -2
Enter score: 7
Enter score: -1
Average score: 8.33
```

### Edge Case (No Valid Scores)

```python
Enter score: -1
No valid scores to average.
```

## Learning Objective

Use an indefinite `while` loop with `break` and `continue`, maintaining totals and counters to compute an average.

## Task Type

Computation + validation + loop control
