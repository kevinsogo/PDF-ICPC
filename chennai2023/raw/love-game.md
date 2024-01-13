<!-- 
** To be edited by problem admin.
        PROBLEM ABSTRACT:
            Eg: given an array of integers, find continuous subarray such that, sum of it's elements is maximum.
                Return the sum of the subarray.
                Egde cases: <add if some cases are must and should be added>
                Stress cases: <add if some cases are must and should be added>
-->


"Internet Club's Passionate Courtship" is a new dating simulator game released by the ICPC.  In it, you are a top competitive programmer looking for love. You can woo various in-game characters, and when you reach a high enough affection with your chosen character, they will become your romantic partner!

Unimportant, but for some odd reason, this game was tagged under the _fantasy_ genre.  You have no idea why, but hope this gets fixed soon!  Anyway...

Each character has some internal integer `x` that determines their level of affection towards you (a negative value means they hate you).  When this value becomes greater than `m`, that character will become your romantic partner.  Giving a character their favorite gift is supposedly the best way to raise affection&mdash;it changes their affection to become one less than the square of their _current_ affection value.  In symbols, if their current affection value is `x`, then after giving them their favorite gift, their affection becomes <code>x<sup>2</sup> - 1</code>.

You can give someone their favorite gift multiple times.  So, suppose your favorite character's affection for you is initially some value `s`.  What is the minimum number of times that you must give them their favorite gift in order to make their affection value `> m`?  If the task is impossible, you must say so as well.



## Input Format

The first line of input contains `t`, the number of test cases. The descriptions of `t` test cases follow.

Each test case consists of a single line containing two space-separated integers, `s` and `m`.


## Output Format

For each test case, output a single line containing:

- an integer denoting the minimum number of times that you must give them their favorite gift in order to make their affection value `> m`; or
- the string `TRY SOMETHING ELSE` if it's impossible.

<br>


## Constraints

- <code>1 ≤ t ≤ 10<sup>5</sup></code>
- <code>0 ≤ s ≤ 10<sup>3</sup></code>
- <code>s ≤ m ≤ 10<sup>5</sup></code>

<br>


## Sample
### Input

```
2
3 7
3 8
```

### Output
```
1
2
```

### Explanation

In both sample test cases, the initial affection level is `s = 3`.

- Giving a gift turns the level into <code>3<sup>2</sup> - 1 = 8</code>.
- Giving a gift turns the level into <code>8<sup>2</sup> - 1 = 63</code>.

<br>

Thus, you need to give `1` gift to make the level `> 7`, and `2` gifts to make the level `> 8`.






