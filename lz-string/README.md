# lz-string Challenge

The challenge details are shown in index.html file

# My Solution:

Because I have a basic understanding with JavaScript, and the mission was to make the
library work in Internet Explorer 6, I ran a google search for "internet explorer 6 common javascript engine issue"
and the second link to the search was a stackoverflow question regrading to 'What are the common mistakes to avoid when coding javascript for Internet Explorer?'

I read the answers to the question until I read [this intresting answer](http://stackoverflow.com/questions/3832292/what-are-the-common-mistakes-to-avoid-when-coding-javascript-for-internet-explor/3838768#3838768)
which made me understand that when running this JavaScript on ie6, the output from [] operator is undefined because ie6 cannot handle this
operator, so I changed the code that included the operator [] to a charAt() function call, which solved the problem.

The code that I replaced was at:

line 22
```javascript
baseReverseDic[alphabet][alphabet.charAt(i)] = i;
```

line 127:
```javascript
context_c = uncompressed.charAt(ii);
```

line 478:
```javascript
entry = w + w.charAt(0);
```

line 486:
```javascript
dictionary[dictSize++] = w + entry.charAt(0);
```

Bonus Mission:
When calling ```javascript _compress(string)``` directly, the browser got stucked because
of endless devilish while loop, in order to understand what happened there, I added an "debug"
messages using ```javascript alert(string)``` function which made me notice that the variable
bitsPerChar - which is nessecary to get out of the loop was undefined! so in order to fix the problem
I replaced the while(true) loop with a for loop that was before the while loop, which produces the same results.
