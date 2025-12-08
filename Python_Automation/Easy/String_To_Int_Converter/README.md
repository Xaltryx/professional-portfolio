# String_To_Int_Converter

A small utility script needs to convert incoming text-based measurements into integers for later processing.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Data](#sample-data)
* [Sample-inputoutput-pairs](#sample-inputoutput-pairs)
* [Learning Objective](#learning-objective)
* [Allowed Libraries](#allowed-libraries)
* [Task Type](#task-type)

## Problem Statement

Write a function `convert_to_int(value)` that takes one argument (a string) and returns its integer form using `int()`.
Then call the function on each item in a sample data list, printing both the original value and the converted result.

If conversion fails for any value, print **"Conversion error"** using `try/except`.

## Sample Data

`["12", "0", "19", "004", "abc"]`

## Sample Input/Output Pairs

```python
Input: "12" → Output: 12
Input: "abc" → Output: "Conversion error"
```

## Learning Objective

Practice calling user-defined functions, using parameters/arguments, using `int()`, and handling simple flow with `try/except`.

## Allowed Libraries

None

## Task Type

Function + validation/error handling using conversion functions
