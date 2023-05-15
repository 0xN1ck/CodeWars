<h3>DESCRIPTION:</h3>

The mean and standard deviation of a sample of data can be thrown off if the sample contains one or many outlier(s) :
<p align="center">
    <img src="http://www.ukoln.ac.uk/web-focus/webwatch/reports/hei-lib-may1998/fig11.gif">
</p>

(<a href="http://www.ukoln.ac.uk/web-focus/webwatch/reports/hei-lib-may1998/report.html">image source</a>)

For this reason, it is usually a good idea to check for and remove outliers before computing the mean or the standard 
deviation of a sample. To this aim, your function will receive a list of numbers representing a <code>sample</code> of
data. Your function must remove any outliers and return the mean of the <code>sample</code>, <b>rounded</b> to 
<b>two</b> decimal places (round only at the end).


Since there is no objective definition of "outlier" in statistics, your function will also receive 
a <code>cutoff</code>, in standard deviation units. So for example if the cutoff is 3, then any value that 
is <b>more</b> than 3 standard deviations above or below the mean must be removed. <i>Notice that, once outlying
values are removed in a first "sweep", other less extreme values may then "become" outliers, that you'll have
to remove as well!</i>

<b>Example:</b>

<pre>
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
cutoff = 3
clean_mean(sample, cutoff) → 5.5
</pre>

<b>Formula for the <a href="https://en.wikipedia.org/wiki/Mean">mean:</a></b>

<p align="left">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/bd2f5fb530fc192e4db7a315777f5bbb5d462c90">
</p>

(where n is the sample size)

<b>Formula for the <a href="https://en.wikipedia.org/wiki/Standard_deviation#Estimation">standard deviation:</a></b>

<p align="left">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/9a937016f00f1978197aa562c5f2d58619f90806">
</p>

(where N is the sample size, xi is observation i and x̄ is the sample mean)

<i>Note : since we are not computing the sample standard deviation for inferential purposes, the denominator is n, 
not n - 1.</i>