<h1>Max From Common DataFrames</h1>

<h3>Input parameters</h3>

<h3>Task</h3>

Your function must return a new <code>pandas.DataFrame</code> with the same data and columns from the first parameter. 
For common columns in both inputs you must return the greater value of each cell for that column.

You must not modify the original inputs.

Input DataFrame will never be empty. The number rows of both inputs will be the same.

<h3>Examples</h3>

<b>Inputs</b>

<pre>
   A    B    C
0  2.5  2.0  2.0
1  2.0  2.0  2.0
</pre>

<pre>
   C    B    D    E
0  1.0  6.0  7.0  1.0
1  8.5  1.0  9.0  1.0
</pre>

<b>Output</b>

<pre>
   A    B    C
0  2.5  6.0  2.0
1  2.0  2.0  8.5
</pre>