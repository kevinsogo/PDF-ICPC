<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->

The idol group Oshikoshi requests that you help design mathematical art for their new album cover.

The album cover is to be a **tree**&mdash;it will showcase the `n` idols, with `n-1` curves that each bidirectionally connect a different pair of idols.  A _simple path_ is a sequence of two or more _distinct_ idols, such that there exists a curve directly connecting any two adjacent idols in the sequence; as it is a tree, there exists a path between any two idols `u` and `v` in the tree, and we can show that such a path is unique.  Thus, you can verify that any tree with `n` idols will have `n(n-1)/2` distinct simple paths (if we count the path from `u` to `v` to be "the same as" the path from `v` to `u`).

Oshikoshi gives you some more definitions!

- Each curve's _length_ is some positive integer.
- The "ink cost" of the entire tree is equal to the sum of the lengths of all of its `n-1` curves.
- The length of a simple path is equal to the sum of the lengths of all curves along that path.
- The _squared length_ of a path is the value you get by taking the length of a path and then squaring it
  - Note that the _sum_ of the lengths of the curves along a path is squared, **not** the individual lengths (e.g. in a path with curves of length `3` and `4`, what we want is <code>(3+4)<sup>2</sup></code> and **not** <code>3<sup>2</sup> + 4<sup>2</sup></code>).
- The "drama" of a tree is equal to the sum of the squared lengths of all `n(n-1)/2` distinct simple paths in the tree.

<br>

Now, the "shape" of the tree has already been decided (i.e. which idols are connected by the `n-1` curves), but the length to make each curve _has not yet been set in stone_.

Here was your original job:  Given an integer `c`, consider all the different ways to assign a positive integer length to each curve in the tree, such that the ink cost is exactly equal to `c`.  Among all such ways, find one which minimizes the drama of the tree; let this minimum drama value be denoted by `m(c)`.

But Oshikoshi wants to mess with you, so they ask you the following question instead:  Given an integer `C`, what is the sum of <code>(m(c))<sup>3</sup></code> across all integers `c` from `n-1` to `C` (inclusive)? Find this number modulo `998244353`.


## Input Format

The first line of input contains `t`, the number of test cases. The descriptions of `t` test cases follow.

The first line of each test case contains two space-separated integers `n` and `C`. Then `n-1` lines follow, each containing two space-separated integers between `1` and `n` denoting a pair of idols directly connected by a curve. We number the idols `1` to `n`.


## Output Format

For each test case, output a single line containing a single integer denoting the answer for that test case.


## Constraints

- <code>&nbsp; 1 ≤ t ≤ 4</code>
- <code>&nbsp; 2 ≤ n ≤ 3·10<sup>5</sup></code>
- <code>n-1 ≤ C ≤ 5·10<sup>7</sup></code>

<br>


## Sample

### Input
```
2
4 3
1 4
1 3
2 1
4 4
1 4
1 3
2 1
```

### Output
```
3375
25327
```

### Explanation

Both sample test cases feature the same tree.

- For `c = 3`, there is only one way to assign positive integer lengths to all `3` curves such that the ink cost is exactly `3`, and that is to assign `1` to each of them.
    - The drama is then <code>m(3) = 1<sup>2</sup> + 1<sup>2</sup> + 1<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> + 2<sup>2</sup> = 15</code>.
- For `c = 4`, one way to achieve the minimum drama is to assign a length of `2` to the curve connecting idols `1` and `3`, and assign a length of `1` to the remaining two curves.
    - The drama is then <code>m(4) = 1<sup>2</sup> + 2<sup>2</sup> + 1<sup>2</sup> + 3<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup> = 28</code>.

<br>

Thus,

- the answer to the first sample case is <code>15<sup>3</sup> mod 998244353 = 3375</code>; and
- the answer to the second sample case is <code>(15<sup>3</sup> + 28<sup>3</sup>) mod 998244353 = 25327</code>.

<br>






