<b>DESCRIPTION:</b>

<p align="center">
    <img src="http://i.imgur.com/zlXr2na.jpg?1">
</p>

Suppose that we roll dice that we never used, a tetrahedral die that has only 4 sides(values 1 to 4), or perhaps better the dodecahedral one with 12 sides and 12 values (from 1 to 12), or look! an icosahedral die with 20 sides and 20 values (from 1 to 20).


Let's roll dice of same type and try to see the distribution of the probability for all the possible sum values.


Suppose that we roll 3 tetrahedral dice:

<pre>
Sum   Prob    Amount of hits           Combinations
3   0.015625     1             {1,1,1}
4   0.046875     3             {1,2,1},{2,1,1},{1,1,2}
5   0.09375      6             {3,1,1},{1,1,3},{1,2,2},{1,3,1},{2,2,1},{2,1,2}
6   0.15625     10             {2,2,2},{1,3,2},{3,2,1},{1,4,1},{2,1,3},{1,1,4},{4,1,1},{3,1,2},{1,2,3},{2,3,1}
7   0.1875      12             {2,3,2},{1,2,4},{2,1,4},{1,4,2},{3,2,2}, {4,2,1},{3,3,1},{3,1,3},{2,2,3},{4,1,2},{2,4,1},{1,3,3}
8   0.1875      12             {2,3,3},{3,3,2},{2,2,4},{4,3,1},{2,4,2},{4,1,3},{4,2,2},{3,4,1},{1,3,4},{3,2,3},{3,1,4},{1,4,3}
9   0.15625     10             {3,3,3},{4,4,1},{2,4,3},{4,2,3},{4,3,2},{1,4,4},{4,1,4},{3,4,2},{2,3,4},{3,2,4}
10  0.09375      6             {3,4,3},{4,4,2},{3,3,4},{4,2,4},(2,4,4),{4,3,3}
11  0.046875     3             {4,3,4},{3,4,4},{4,4,3}
12  0.015625     1             {4,4,4}
tot: 1.0000
</pre>

Note that the total sum of all the probabilities for each end has to be <code>1.0000</code>

The register of hits per each sum value will be as follows:

<pre>
[[3, 1], [4, 3], [5, 6], [6, 10], [7, 12], [8, 12], [9, 10], [10, 6], [11, 3], [12, 1]]
</pre>

Create the function <code>reg_sum_hits()</code> that receive two arguments:

* number of dice, n
* number of sides of the die, s

The function will output a list of pairs with the sum value and the corresponding hits for it.

For the example given above:
<pre>
reg_sum_hits(3, 4) == [[3, 1], [4, 3], [5, 6], [6, 10], [7, 12], [8, 12], [9, 10], [10, 6], [11, 3], [12, 1]]
</pre>

You will find more examples in the Example Test Cases.

Assumption: If the die has n sides, the values of it are from <code>1</code> to <code>n</code>