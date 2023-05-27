<b>DESCRIPTION:</b>

According to <a href="https://en.wikipedia.org/wiki/Gary_Chapman_(author)">Gary Chapman</a>, 
marriage counselor and the author of <a href="https://en.wikipedia.org/wiki/The_Five_Love_Languages">
"The Five Love Languages"</a> books, there are five major ways to express our love towards someone:
<i>words of affirmation, quality time, gifts, acts of service, and physical touch.</i> 
These are called the love languages. Usually, everyone has a main language: the one that he/she "speaks" 
and understands best. In a relationship, it's import to find your partner's main love language, so that you 
get along better with each other.

<b>Your task</b>

Unfortunately, your relationship got worse lately... After a long discussion with your partner, you agreed 
to give yourself a few weeks to improve it, otherwise you split up...

You will be given a <code>partner</code> instance, and <code>n</code> weeks. The <code>partner</code> 
has a <code>.response</code> method, and the responses may be: <code>"positive"</code> or <code>"neutral"</code>. 
You can try to get a response once a day, thus you have <code>n * 7</code> tries in total to find the 
main love language of your partner!

The love languages are: <code>"words", "acts", "gifts", "time", "touch"</code> (available 
predefined as <code>LOVE_LANGUAGES</code>)

Note: your partner may (and will) sometimes give a positive response to any love language ("false positive"), 
but the main one has a much higher possibility. On the other hand, you may get a neutral response even for 
the main language, but with a low possibility ("false negative").

There will be 50 tests. Although it's difficult to fail, in case you get unlucky, just run the tests again. 
After all, a few weeks may not be enough...

<b>Examples</b>

<pre>
main love language: "words"

partner.response("words")  -->  "positive"
partner.response("acts")   -->  "neutral"
partner.response("words")  -->  "positive"
partner.response("time")   -->  "neutral"
partner.response("acts")   -->  "positive"    # false positive
partner.response("gifts")  -->  "neutral"
partner.response("words")  -->  "neutral"     # false negative
etc.
</pre>

Happy coding, and DO try this at home! :-)