<b>DESCRIPTION:</b>

You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. 
Each time you get a string of all race results of every team who has run. For example here is a string showing 
the individual results of a team of 5 runners:

<code>"01|15|59</code>, <code>1|47|6</code>, <code>01|17|20</code>, <code>1|32|34</code>, <code>2|3|17"</code>

Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive 
or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ,  
or ,.

To compare the results of the teams you are asked for giving three statistics; range, average and median.

<b>Range :</b><br> difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and 
the highest is 9, so the range is 9 − 3 = 6.

<b>Mean or Average :</b><br> To calculate mean, add together all the numbers and then divide the sum by the total 
count of numbers.

<b>Median :</b><br> In statistics, the median is the number separating the higher half of a data sample from 
the lower half. The median of a finite list of numbers can be found by arranging all the observations from 
the lowest value to the highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) 
when there is an odd number of observations. If there is an even number of observations, then there is no single 
middle value; the median is then defined to be the mean of the two middle values 
(the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above, the string result will be

<code>"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"</code>

of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

where hh, mm, ss are integers (represented by strings) with each 2 digits.

<b>Remarks:</b><br>
<i>if a result in seconds is ab.xy... it will be given truncated as ab.</i><br>
<i>if the given string is "" you will return ""</i>