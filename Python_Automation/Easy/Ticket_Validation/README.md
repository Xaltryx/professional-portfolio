# Ticket_Validation

A helpdesk tool needs to quickly check whether a reported ticket number is valid.

## Table of Contents

* [Problem Statement](#problem-statement)
* [Sample Data](#sample-data)
* [Sample Input/Output](#sample-inputoutput)
* [Learning Objective](#learning-objective)
* [Allowed Libraries](#allowed-libraries)
* [Task Type](#task-type)

## Problem Statement

Write a program that asks the user for a ticket number and determines whether it is valid.
A valid ticket number is an integer greater than **0**.
Use a Boolean expression and an `if` statement to print either **"Valid ticket"** or **"Invalid ticket"**.

## Sample Data

**Normal case:**
`27`

**Edge cases:**
`0`
`-5`

## Sample Input/Output

**Normal Case:**

```python
Enter ticket number: 27
Valid ticket
```

**Edge Case (0):**

```python
Enter ticket number: 0
Invalid ticket
```

**Edge Case (Negative):**

```python
Enter ticket number: -5
Invalid ticket
```

## Learning Objective

Use Boolean expressions, comparison operators, and simple conditional execution.

## Allowed Libraries

None

## Task Type

Validation using Boolean expression and `if`
