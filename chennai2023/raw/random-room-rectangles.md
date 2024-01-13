<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->


You want to redecorate a square room of dimensions <code>n &times; n</code> with tiles. The room can be divided into <code>n<sup>2</sup></code> blocks of dimensions <code>1 &times; 1</code>. You also have <code>n<sup>2</sup></code> tiles of dimensions <code>1 &times; 1</code> available with you.

Each tile has a blue line running across exactly one of its diagonals and may be placed in two orientations as shown below -

![Orientations](https://storage.googleapis.com/cdcontent/contents/3106/attachments/assets/Tiles.png)

For each block, you will choose a tile and place it in the block. For each of the tiles, you can choose one of the above two orientations randomly, uniformly and independently. You task is to find the **expected number of rectangles formed by the blue diagonal lines**. 

Note that a single diagonal can be a part of multiple rectangles. For example, the following arrangement contains <code>8</code> rectangles (<code>4</code> rectangles of size <code>&Sqrt;2 &times; &Sqrt;2</code>, <code>2</code> rectangles of size <code>2&Sqrt;2 &times; &Sqrt;2</code>, <code>1</code> rectangle of size <code>&Sqrt;2 &times; 2&Sqrt;2</code> and <code>1</code> rectangle of size <code>3&Sqrt;2 &times; &Sqrt;2</code>).

![Example Grid](https://storage.googleapis.com/cdcontent/contents/3106/attachments/assets/Example-Grid.png)


## Input Format

The first line of input contains an integer <code>t</code> denoting the number of test cases.

Each test case consists of a single line containing an integer <code>n</code>.


## Output Format

For each test case, print a single line containing a single integer denoting the expected number of rectangles formed by the blue diagonal lines "modulo `998244353`". In more detail:

- It can be shown that the answer can uniquely be expressed as a fraction <code><sup>p</sup>/<sub>q</sub></code> where <code>p</code> and <code>q</code> are integers, `q` is positive, and `p` and `q` are relatively prime.
- It can also be shown under the constraints of this problem that for any such fraction, there is a unique `r` mod `998244353` such that `p ≡ qr` mod `998244353`.
- The required output is this unique `r` mod `998244353`. (And we write "<code><sup>p</sup>/<sub>q</sub> ≡ r mod 998244353</code>".)

<br>


## Constraints  

- <code>1 &le; t &le; 10<sup>5</sup></code>
- <code>1 &le; n &lt; 998244353</code>

<br>


## Sample

### Input
```
3
1
2
3
```

### Output
```
0
935854081
717488129
```

### Explanation

There is no way to form a rectangle in a <code>1 &times; 1</code> grid. So, the expected number of rectangles is <code>0</code>.

For a <code>2 &times; 2</code> grid, there are <code>16</code> possible arrangements of tiles. Out of them, only the following arrangement contains a rectangle of size <code>&Sqrt;2 &times; &Sqrt;2</code>:

![Sample Case 2](https://storage.googleapis.com/cdcontent/contents/3106/attachments/assets/Sample-Case-2.png)

So, the expected number of rectangles is <code><sup>1</sup>/<sub>16</sub> &Congruent; 935854081 (mod 998244353)</code>.

For test case 3, the actual expected number of rectangles is <code><sup>9</sup>/<sub>32</sub> &Congruent; 717488129 (mod 998244353)</code>.




