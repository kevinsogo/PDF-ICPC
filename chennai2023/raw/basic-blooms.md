<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->

In a hidden realm where numbers dance and bases intertwine, there exists a garden of exquisite beauty known as the Number Garden. Within its vibrant meadows, a unique species of flowers flourishes&mdash;the Basic Bloom.

Each Basic Bloom flower contains some petals. Basic Blooms are unique because their number of petals can be expressed as a sequence of a single digit **one or more times**, in **at least one base** between `2` and `16` (inclusive).
Digits beyond `9` are represented in lexicographic order of the English alphabet. Specifically, `10` is represented as `a`, `11` as `b`, `12` as `c` and so on.

For example:

- a flower with `14` petals is a Basic Bloom because `14` can be represented as `22` in base `6` or `e` in base `15`.
- a flower with `10` petals is a Basic Bloom because `10` can be represented as `11` in base `9`.
- a flower with `931` petals is a Basic Bloom because `931` can be represented as `777` in base `11`.
- a flower with `1570` petals is a Basic Bloom because `1570` can be represented as `aaa` in base `12`.

<br>

Notably, and for each positive integer `x` that can be expressed as a single digit in at least one base between `2` and `16`, there is at least one Basic Bloom with `x` petals. Also, no two Basic Blooms have the same number of petals.

The Guardians of the Garden, seeking to share the wonders of this numerical symphony, have issued a challenge to code wizards across the realms. They seek those who can harness the power of algorithms and traverse the Garden's mathematical pathways.

The challenge is as follows:
Arrange all the Basic Bloom flowers in increasing order of number of petals. Given <code>k<sub>1</sub></code> and <code>k<sub>2</sub></code>, find the **sum of the number of petals** from the <code>k<sub>1</sub></code>th flower to the <code>k<sub>2</sub></code>th flower modulo `998244353`.

In other words, let <code>p<sub>i</sub></code> denote the number of petals in the `i`th flower. Find the sum of <code>p<sub>i</sub></code> for `i` from  <code>k<sub>1</sub></code> to <code>k<sub>2</sub></code> modulo `998244353`.


## Input Format

- The first line of of the input contains an integer `t` denoting the number of test cases.
- Each test case is a single line containing two space-separated integers <code>k<sub>1</sub></code> and <code>k<sub>2</sub></code>.

<br>


## Output Format

- For each test case, print a single line containing the answer as described in the statement.

<br>


## Constraints

- <code>1 ≤ t ≤ 10<sup>6</sup></code>
- <code>1 ≤ k<sub>1</sub> ≤ k<sub>2</sub> ≤ 10<sup>6</sup></code>

<br>


## Sample

### Input
```
3
1 2
1 10
15 2000
```

### Output
```
3
55
736374621
```

### Explanation

The first few Basic Blooms have the following number of petals:

```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20,
21, 22, 24, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 39, 40, 42, 43,
44, 45, 48, 50, 51, 52, 54, 55, 56, 57, 60, 62, 63, 64, 65, 66, 68,
70, 72, 73, 75, 77, 78, 80, 84, 85, 86, 88, 90, 91, 93, 96, 98, 99,
...]
```



