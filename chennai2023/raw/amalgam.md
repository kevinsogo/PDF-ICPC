<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->

You need a new name for your pet dog, and you want it to be extraordinary!

You have a list of `n` possible names <code>s<sub>1</sub></code>, <code>s<sub>2</sub></code>, ..., <code>s<sub>n</sub></code>. Each name is a nonempty string consisting of lowercase English letters. These names are not necessarily distinct.

However, your dog's name will not necessarily be one of the <code>s<sub>i</sub></code>'s. Instead, it will be an *amalgamation* of two such strings. Specifically, it will be one of the <code>n<sup>2</sup></code> (not necessarily distinct) names <code>s<sub>x</sub> + s<sub>y</sub></code> (`1 ≤ x, y ≤ n`) formed by concatenating two such strings.

You have sorted these <code>n<sup>2</sup></code> names according to the following order:

- You think shorter names are nicer, so shorter names appear before longer names.
- Names of equal length are arranged alphabetically.

<br>

You then numbered these names <code>1</code> to <code>n<sup>2</sup></code>, in this sorted order. Finally, you have decided that the name of your dog will be the `k`th name in this list, with <code>1 ≤ k ≤ n<sup>2</sup></code>.

Given `k`, what is the `k`th name in this list?

Actually, you still haven't decided on `k` yet, so you need to answer this question `m` times, each with a possibly different value of `k`.


## Input Format

The first line contains two space-separated integers `n` and `m`.

The `i`th of the next `n` lines contains the string <code>s<sub>i</sub></code>.

The next and final line contains `m` space-separated integers <code>k<sub>1</sub></code>, <code>k<sub>2</sub></code>, ..., <code>k<sub>m</sub></code>.


## Output Format

Print `m` lines. The `i`th line must contain two space-separated integers `x` and `y`, where <code>s<sub>x</sub> + s<sub>y</sub></code> is the answer if <code>k = k<sub>i</sub></code>.

There may be multiple such pairs `(x, y)` whose concatenation <code>s<sub>x</sub> + s<sub>y</sub></code> produces the same string; any such pair will be accepted.


## Constraints

- <code>2 ≤ n ≤ 10<sup>5</sup></code>
- <code>1 ≤ m ≤ 10<sup>5</sup></code>
- <code>length(s<sub>i</sub>) ≤ 10<sup>5</sup> </code>
- <code>1 ≤ k<sub>i</sub> ≤ n<sup>2</sup></code>
- The sum of <code>length(s<sub>i</sub>)</code> in a single test file `≤ 250000`

<br>


## Sample

### Input
```
3 9
b
aa
aa
1 2 3 4 5 6 7 8 9
```

### Output
```
1 1
3 1
2 1
1 2
1 3
2 3
3 3
2 2
3 2
```

### Explanation

The <code>3<sup>2</sup> = 9</code> names are:

- `b  +  b   = bb`
- `b  +  aa  = baa`
- `b  +  aa  = baa`
- `aa +  b   = aab`
- `aa +  aa  = aaaa`
- `aa +  aa  = aaaa`
- `aa +  b   = aab`
- `aa +  aa  = aaaa`
- `aa +  aa  = aaaa`

<br>

Sorting according to the order described above, we get `[bb, aab, aab, baa, baa, aaaa, aaaa, aaaa, aaaa]`.

Note that the output is not necessarily unique. Here's another valid output:
```
1 1
3 1
3 1
1 3
1 3
2 2
2 2
3 3
2 2
```



