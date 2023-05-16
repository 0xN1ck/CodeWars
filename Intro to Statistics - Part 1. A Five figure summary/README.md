<h3>DESCRIPTION:</h3>

<h5>Background</h5>

A simple statistical analysis of a series of samples can be done with a 
<a href="http://en.wikipedia.org/wiki/Five-number_summary">Five Figure Summary.</a>

The five figure summary gives the lower extreme, upper extreme, lower quartile, median, and upper quartile, all 
derived from the supplied sample data.

Confusingly, the five figure summary often includes a sixth value, which is the number of samples in the series.


<h5>Kata</h5>

In this Kata you will be given a class outline to complete. The class will be instantiated with a sequence of values, 
and you must implement the method to return the six-figure version of a five figure summary.

You are expected to do the calculations yourself, using pandas or numpy will get you a squinty frown from your sensei! :)


<h5>Inputs</h5>

1. At class instantiation you will be given a sequence of values. This sequence may contain non-numerical values: 
these should be ignored. 
2. At summary creation you will be given a maximum number of decimal digits precision for all the numerical results. 
If None is supplied, assume full precision has to be returned.


<h5>Calculations</h5>

* N: Number of valid numeric values in the sequence.
* Lower Extreme: The smallest value contained within the sequence.
* Upper Extreme: The largest value contained within the sequence.
* Median: The centre value of the sorted sequence of valid values.
* Lower Quartile: The boundary value between the first and second quarters of the sorted sequence of valid values.
* Upper Quartile: The boundary value between the third and fourth quarters of the sorted sequence of valid values.

The median and both quartiles may need to be a linear interpolation between two values.


<h5>Linear Interpolation Examples</h5>

Given a sequence of values <code>[2, 3, 4, 5, 6, 7, 8, 9]</code>

1. Position 3.5 would return the mid-point between the values at index 3 and index 4 returning 5.5.
2. Position 1.25 would return the quarter-point between the values at index 1 and index 2 returning 3.25.
3. Position 6.75 would return the three-quarter-point between the values at index 6 and index 7 returning 7.75.


<h5>Outputs</h5>

You will return a tuple with the calculated values in the following order:

<pre>
(N, lower_extreme, upper_extreme, lower_quartile, median, upper_quartile)
</pre>

Where no precision is defined, and given the rounding/quantization errors with floating point processing, 
your answers must be within <code>10 ** -10</code> of the correct answer. Where precision is defined, 
your answer is expected to be exact.


<h5>Worked Example</h5>

<pre>
data = range(0, 7)
StatisticalSummary(data).five_figure_summary(2)   =>   (7, 0, 6, 1.5, 3, 4.5)
</pre>

