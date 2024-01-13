<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->

You have an <code>n &times; n</code> hexagonal chessboard where <code>n<sup>2</sup></code> hexagonal cells are arranged in <code>n</code> rows, each having <code>n</code> cells in a 2-dimensional hexagonal closed packing manner. The figure given below shows a <code>7 &times; 7</code> hexagonal chessboard. The bottom-most row is always half a cell to the left of the second row from the bottom. There are <code>6</code> directions as shown by the red arrows in the figure.

A horsey is a chess piece that can move as follows: Move <code>2</code> cells in direction <code>i</code> and then <code>1</code> cell in direction <code>j</code> such that <code>|i-j| mod 3 &ne; 0</code>. Note that only the source and destination cells in a move are counted as visited by the horsey. The intermediate cells are not visited and may not even exist on the chessboard. For example, in the given figure, if a horsey is present in the black cell, it can move to any of the blue cells.

![horsey moves](https://storage.googleapis.com/cdcontent/contents/3105/attachments/assets/example.png)

Your task is to find a path that a horsey should follow in order to visit all cells in the chessboard **exactly once** or determine if no such path exists. Since horseys are one of the laziest species in chess, they prefer shorter paths and paths where the starting and ending cells are adjacent to each other. So, if there are multiple answers, find the **path with the shortest length such that the first and the last cell of the path are adjacent to each other** (share a boundary with each other). The distance between two cells is the Euclidean distance between their centers. If there are still multiple answers, you may find any.


## Input Format

The first line of input contains an integer <code>t</code> denoting the number of test cases.

Each test case consists of a single line of input containing an integer <code>n</code>.


## Output Format

For each test case:

- If no such path exists, print a single line containing the integer <code>-1</code>.

- Otherwise, print the path as follows.

    - Let the <code>y</code>th cell from the left in the <code>x</code>th row from the bottom be represented as <code>(x,y)</code>.
    - The horsey's path can be described by <code>n<sup>2</sup></code> distinct cells <code>(x<sub>1</sub>,y<sub>1</sub>), (x<sub>2</sub>,y<sub>2</sub>), (x<sub>3</sub>,y<sub>3</sub>), ..., (x<sub>n<sup>2</sup></sub>,y<sub>n<sup>2</sup></sub>)</code>, in the order they are visited.
    - You need to print <code>2</code> lines, the first line containing the values <code>x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>n<sup>2</sup></sub></code> and the second line containing the values <code>y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, ..., y<sub>n<sup>2</sup></sub></code>.

<br>


## Constraints

- `1 ≤ t ≤ 1000`
- `2 ≤ n ≤ 1024`
- The sum of <code>n<sup>2</sup></code> across all test cases does not exceed `1048576`

<br>


## Sample

### Input
```
2
2
4
```

### Output
```
-1
1 2 4 3 1 3 4 3 1 2 4 2 3 4 2 1
2 3 3 2 4 4 2 1 1 2 4 4 3 1 1 3
```

### Explanation

The path followed by the horsey in the second test case is shown in the image below:

![sample-2](https://storage.googleapis.com/cdcontent/contents/3105/attachments/assets/4x4-Sample.png)

The numbers given represent the order in which the cells are visited in the path.


