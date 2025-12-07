# User_Access_Control

A small access-control script must determine the correct message to show different types of users.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Data](#sample-data)
* [Sample Input/Output](#sample-inputoutput)
* [Learning Objective](#learning-objective)
* [Allowed Libraries](#allowed-libraries)
* [Task Type](#task-type)

## Problem Statement

Write a program that asks for two inputs:

* A username (string)
* A role level (integer)

Use `if` / `elif` / `else` with logical operators to print:

* `"Admin access granted"` if role is **5** and username is not empty
* `"Standard access"` if role is between **1 and 4**
* `"Guest access only"` if role is **0**
* `"Invalid role"` for negative numbers or any other unexpected value

## Sample Data

**Normal cases:**

* username = `"Clara"`, role = `5`
* username = `"Eli"`, role = `3`

**Edge cases:**

* username = `""`, role = `5`
* username = `"Sam"`, role = `-1`

## Sample Input/Output

**Normal Case (Admin):**

```python
Enter username: Clara
Enter role level: 5
Admin access granted
```

**Normal Case (Standard):**

```python
Enter username: Eli
Enter role level: 3
Standard access
```

**Edge Case (Empty Username):**

```python
Enter username: 
Enter role level: 5
Invalid role
```

**Edge Case (Negative Role):**

```python
Enter username: Sam
Enter role level: -1
Invalid role
```

## Learning Objective

Chained conditionals, logical operators (`and`, `or`), and robust branching logic.

## Allowed Libraries

None

## Task Type

Conditionals, validation, logic
