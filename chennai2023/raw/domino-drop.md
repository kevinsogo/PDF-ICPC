<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->

There are `n` dominos of various heights placed in a row from left to right. When you tip the first domino towards the right, it causes a chain reaction. If the height of the `i`th domino is `h`, it will knock down all dominos in the range `[i, i + h - 1]` (i.e., all the dominos `x` such that `i ≤ x < i + h` will fall). For example, if `h = 1`, then no additional domino will fall, but if `h = 2`, the next domino will fall. Also, a domino falling upon another will trigger the chain reaction on that domino as well.

Suppose you can increase the height of the first domino by an arbitrary amount. You are curious and are thinking about what additional height should be added to the first domino to make at least `k` dominos fall. What is the minimum additional height needed to do this? Answer this for each `k` from `1` to `n`. 

Note that the height of any domino must always be an integer.


## Input Format

- The first line of of the input contains an integer `t` denoting the number of test cases.
- The first line of each test case contains an integer, `n` representing the number of dominos.
- The second line of each test case contains `n` space-separated integers, each representing the height of the corresponding domino.

<br>


## Output Format

- For each test case, output `n` space-separated integers denoting the answers in order, for `k` from `1` to `n`.

<br>


## Constraints

- <code>1 &le; t &le; 10<sup>5</sup></code>
- <code>1 &le; n &le; 10<sup>5</sup></code>
- The height of each domino is a positive integer <code>&le; 10<sup>9</sup></code>
- Sum of `n` over all the test cases won't exceed <code>4·10<sup>5</sup></code>

<br>


## Sample

### Input
```
3
5
2 1 3 1 2
4
2 2 2 1
3
1 1 1
```

### Output
```
0 0 1 1 1
0 0 0 0
0 1 2
```

### Explanation

For the first test case:

- The first domino falling will also cause the next domino to fall.
- The second domino falling will **not** cause the next one to fall.
- Thus, to make 1 and 2 dominos fall, you don't need to add any additional height to the first domino.
- Suppose the height of the first domino was additionally increased by 1, i.e., it was 3. Then, the first domino will make the second and third dominos fall as well. The third domino will also make the fourth and fifth dominos fall. Thus, for `k = 3, 4, 5`, the answer would be 1.

<br>



