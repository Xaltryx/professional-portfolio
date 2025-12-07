# Shipment_Quality_Check

A warehouse quality-checker wants to review a list of shipment quantities and safely evaluate the data.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Data](#sample-data)
* [Sample Input/Output](#sample-inputoutput)
* [Learning Objective](#learning-objective)
* [Allowed Libraries](#allowed-libraries)
* [Task Type](#task-type)

## Problem Statement

You are given a list of quantities entered one at a time by the user, ending when they type **-1**.

After collecting the list:

* Use a **guardian pattern (short-circuit evaluation)** to avoid dividing by zero.
* Use **try/except** to handle any input that cannot be converted to an integer.

Print:

* `"All quantities acceptable"` if all items are ≥ 0
* `"Contains defective items"` if any quantity is negative (other than -1 stop flag)
* `"No data to evaluate"` if the list is empty

## Sample Data

**Normal case:**
`[12, 8, 0, 4, 3, 9]` → all acceptable

**Edge cases:**
`[]` → empty
`[5, -2, 7]` → defective item exists
`["abc", 7]` → requires try/except handling

## Sample Input/Output

**Normal Case:**

```python
Enter quantity (-1 to stop): 12
Enter quantity (-1 to stop): 8
Enter quantity (-1 to stop): 0
Enter quantity (-1 to stop): 4
Enter quantity (-1 to stop): 3
Enter quantity (-1 to stop): 9
Enter quantity (-1 to stop): -1
All quantities acceptable
```

**Edge Case (Defective Item):**

```python
Enter quantity (-1 to stop): 5
Enter quantity (-1 to stop): -2
Enter quantity (-1 to stop): 7
Enter quantity (-1 to stop): -1
Contains defective items
```

**Edge Case (Invalid Input / Empty):**

```python
Enter quantity (-1 to stop): abc
Invalid entry skipped.
Enter quantity (-1 to stop): -1
No data to evaluate
```

## Learning Objective

Short-circuit evaluation (guardian pattern), try/except, nested conditionals, input validation.

## Allowed Libraries

None

## Task Type

Validation/error handling, logical operators, nested conditionals, short-circuit safety
