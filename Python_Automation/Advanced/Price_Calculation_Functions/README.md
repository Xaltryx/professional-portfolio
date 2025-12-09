# Price_Calculation_Functions

A workplace script needs reusable functions for calculating item totals, tax, and formatted output.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Data](#sample-data)
* [Sample Input/Output](#sample-inputoutput)
* [Learning Objective](#learning-objective)
* [Allowed Libraries](#allowed-libraries)
* [Task Type](#task-type)

## Problem Statement

Write three functions:

### `calc_subtotal(prices)`

* `prices` is a list of numbers
* returns the sum **manually using a loop** (not `sum()`)

### `calc_tax(subtotal, rate)`

* returns `subtotal * rate`
* ensure both arguments are numbers using `type()`; if not, return `None`

### `format_total(total)`

* returns a string version of `total` using `str()`

Then call the three functions together to compute the final price for the sample data.
If subtotal is **0** (empty list), print **"No items to process"**.

## Sample Data

Normal case:
`[12.5, 5.0, 19.0, 3.5]`

Edge case:
`[]`

## Sample Input/Output

**Normal Case:**

```python
subtotal: 40.0
tax: 4.0
total string: "44.0"
```

**Edge Case:**

```python
No items to process
```

## Learning Objective

Combine fruitful functions, parameter passing, type checking, manual accumulation with loops, string conversion, and modular program design.

## Allowed Libraries

None

## Task Type

Modular design + algorithmic reasoning + validation + type handling
