# Algorithms

I am currently brushing up a bit on my CS background. I also want to learn Python. So here I implement some common algorithms in Python.

This online course helps me along the way: https://lagunita.stanford.edu/courses/course-v1:Engineering+Algorithms1+SelfPaced

## Asymptomic Analysis

_Big Oh-notation_ , e.g. `O(n log n)` where n = input size

The Big-Oh function defines the worst-case running time of an algorithm.

T(n) = O(f(n))

- suppress constant factors (too system dependant)
- ignore lower-order terms (irrelevant for large inputs)

### Simplest example: Search array A for the integer t.

Does A contain t?
Linear --> O(n)

Search arrays A, B for the integer t.
Does A or B contain t?
Linear --> O(n)
_even though the number of operations is roughly 2 times the number of searching only one array, it is still linear, hence we just define the complexity with O(n)_

### Example: Two nested loops

Do arrays A, B have a number in common?
Quadratic --> O(n^2)

Does Array A have duplicate entries?

```
    for i = 1 to n
        for j = i + 1 to n
         if A[i] == A[j] return TRUE
    return FALSE
```

Quadratic --> O(n^2)

**_MANTRA: Can we do better?_**

When writing an algorithm we should always ask ourselves "can we do better?".

## DIVIDE AND CONQUER

Seperate (split) input value n and solve each part recursively.
At the end, compute result from sub-results.
