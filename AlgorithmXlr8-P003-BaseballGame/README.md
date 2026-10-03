<p align="center"><img src="https://algorithmxlr8.io/logo-mark.png" width="56" alt="AlgorithmXlr8.io logo" /></p>
<h3 align="center">AlgorithmXlr8.io</h3>
<p align="center"><sub>Solved and synced automatically from <a href="https://algorithmxlr8.io">AlgorithmXlr8.io</a></sub></p>

---

# Baseball Game

**Difficulty:** `Easy`

## Problem

You are keeping the scores for a baseball game with strange rules. Given a list of operations ops, where each string is either an integer (record a new score), "+" (record the sum of the previous two scores), "D" (record double the previous score), or "C" (invalidate/remove the previous score), return the sum of all scores on the record after applying all operations.

Read n and the n operations (each on its own line) from standard input. Print the sum of all remaining scores.

## Examples

### Example 1

**Input**
```
5
5
2
C
D
+
```
**Output**
```
30
```

**Explanation:** 5, 2, remove 2, double 5 (10), sum of previous two (5+10=15): record is [5,10,15], summing to 30.

### Example 2

**Input**
```
8
5
-2
4
C
D
9
+
+
```
**Output**
```
27
```

**Explanation:** The record ends as [5,-2,-4,9,5,14], summing to 27.

---

Solved on [AlgorithmXlr8.io](https://algorithmxlr8.io/solve-dsa/baseball-game).