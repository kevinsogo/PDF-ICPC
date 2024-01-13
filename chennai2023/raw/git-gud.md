<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->

Loid is teaching Anya about implicit data structures for the Eden Academy entrance exam, as this is important knowledge that all 6-year olds must know (of course, Anya doesn't know any of this yet because she is only 5 years old).

He is explaining how version control systems can compress lots of information by only storing what has _changed_ from version to version.  As an illustrative example, he tells Anya that they are going to build `n+1` different arrays in the following manner.

Firstly, let `A(0)` be the empty array.  He then makes `n` "commits", labeled from `1` to `n`.  The `i`th commit describes an array `A(i)`, which is formed by appending one element to the end of the array in some previous commit.  Specifically, the `i`th commit is totally described by two values <code>j<sub>i</sub></code> and <code>x<sub>i</sub></code>, meaning that <code>A(i)</code> is the array you get by appending <code>x<sub>i</sub></code> to the end of array <code>A(j<sub>i</sub>)</code>.  The magic here is that arrays `A(1)` through `A(n)` can describe `n` different sequences&mdash;each of whose length is bounded by `O(n)`&mdash;but it only needs a total of `O(n)` space overall!

Now, Loid warns Anya that she must be able to answer the following question, since he has insider knowledge that it will appear on the entrance exam.  Anya must compute the value of <code>g<sub>i</sub></code>, which is defined to be the sum of the GCDs of all subarrays of array `A(i)`, taken modulo `998244353`, where the value of `i` will be revealed on the day of the exam.

But Anya can't do this!  So instead, she asks you to compute **all values** of <code>g<sub>i</sub></code> for each `i` from `1` to `n` for her, and then she will just memorize _all of them_ in preparation for the test.  Please help her get into Eden Academy!

**Notes:**

- The values <code>j<sub>i</sub></code> and <code>x<sub>i</sub></code> are given in an unusual way; see the input format for more details.
- The **greatest common divisor**, or **GCD**, of an array of numbers is the largest positive integer that divides all the elements of the array.

<br>


## Input Format

The first line contains a single integers `n`.

The `i`th of the next `n` lines contains two nonnegative integers <code>J<sub>i</sub></code> and <code>X<sub>i</sub></code>. The numbers <code>j<sub>i</sub></code> and <code>x<sub>i</sub></code> are then computed as follows:

- <code>j<sub>i</sub> = g<sub>i-1</sub> ⊕ J<sub>i</sub></code>
- <code>x<sub>i</sub> = g<sub>i-1</sub> ⊕ X<sub>i</sub></code>

<br>

Here, `x ⊕ y` is the bitwise XOR of `x` and `y` and is defined as the result of adding `x` and `y` in base 2 *without* carrying.



## Output Format

Print `n` lines. The `i`th line must contain the integer <code>g<sub>i</sub></code>.


## Constraints

- <code>1 ≤ n ≤ 10<sup>6</sup></code>
- <code>0 ≤ j<sub>i</sub> < i </code>
- <code>1 ≤ x<sub>i</sub> ≤ 10<sup>18</sup></code>

<br>


## Sample

### Input
```
2
0 60
61 48
```

### Output
```
60
84
```

### Explanation

- `A(0)` is the empty array, or `[]`.
- The sum of the GCDs of all subarrays of `[]` is <code>0</code>.
- Therefore, <code>g<sub>0</sub> = 0 mod 998244353 = 0</code>.
- <code>j<sub>1</sub> = g<sub>0</sub> ⊕ J<sub>1</sub> = 0 ⊕ 0 = 0</code>
- <code>x<sub>1</sub> = g<sub>0</sub> ⊕ X<sub>1</sub> = 0 ⊕ 60 = 60</code>
- `A(1)` is the array `A(0) + [60]`, or `[60]`, 
- The sum of the GCDs of all subarrays of `[60]` is <code>60</code>.
- Therefore, <code>g<sub>1</sub> = 60 mod 998244353 = 60</code>.
- <code>j<sub>2</sub> = g<sub>1</sub> ⊕ J<sub>2</sub> = 60 ⊕ 61 = 1</code>
- <code>x<sub>2</sub> = g<sub>1</sub> ⊕ X<sub>2</sub> = 60 ⊕ 48 = 12</code>
- `A(2)` is the array `A(1) + [12]`, or `[60, 12]`, 
- The sum of the GCDs of all subarrays of `[60, 12]` is <code>60 + 12 + 12 = 84</code>.
- Therefore, <code>g<sub>2</sub> = 84 mod 998244353 = 84</code>.

<br>



