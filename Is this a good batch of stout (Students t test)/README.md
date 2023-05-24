<b>DESCRIPTION:</b>

You have been hired by a large stout brewery in order to improve the quality testing of their beer. Your superiors want 
you to devise a way of determining whether a batch of beer is likely to be good enough for sale using a small sample of 
beers from this batch. Luckily for you, a smart Englishman found a solution to this problem a bit more than a hundred 
years ago...

Your task in this kata is to implement a function to do Student's one-sample t-test. In the current problem, you 
will be testing for alcohol content. Your function will receive :

1. A list of the alcohol content of each beer in a sample of beers: <code>sample</code>
2. A target alcohol content: <code>pop_mean</code>
3. A probability threshold: <code>alpha</code>

By calculating a t value for the sample, you will be able to determine whether the current batch is likely to have 
an average alcohol content close to the target, or not. In statistical terms, if the likelihood that the current 
sample of beers was taken from the population of beers with a mean of <code>pop_mean</code> 
(the target alcohol content) is too small (it is too different from the "average" sample), 
then the whole batch will be rejected.

<b>Specifically</b>, your solution will calculate a t statistic (formula below) and compare it to a "critical" t value, 
corresponding to the threshold. You are given a table of critical t values (<code>t_table</code>), containing only 
positive values of t (the t distribution is symmetrical) which you may access like so: 
<code>t_table[degrees_of_freedom - 1][probability]</code>. Degrees of freedom in a one sample t-test are equal to n - 1, 
where n is the sample size. If the sample's t value is greater than the "critical" t value 
(and therefore less probable), then your function will return "Reject". Else, your function will return 
"Good to drink". All samples will range in size from 2 to 20.

<b>Formula for the</b> <a href="https://en.wikipedia.org/wiki/Student%27s_t-test">t statistic</a>:

<p align="left">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1063f91f450e9fd0094a38f1856eb11bd201d232">
</p>

Where x̄ is the sample mean, μ0 is the population mean, s is the sample standard deviation and n is the sample size.

<b>Formula for the</b> 
<a href="https://en.wikipedia.org/wiki/Standard_deviation#Estimation"> 
sample standard deviation (s)</a>:

<p align="left">
    <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/1bffdcb1ecd0b326bb7ad67397b073af9c15fa6e">
</p>

Where N is the sample size, xi is observation i and x̄ is the sample mean.

Kata inspired by <a href="https://priceonomics.com/the-guinness-brewer-who-revolutionized-statistics/">this</a>.