"""Regular Expressions

A regular expression or RegEx is a special text string that helps to find patterns in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is called re.
"""

"""The re Module

After importing the module we can use it to detect or find patterns."""

import re

"""Methods in re Module

To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string"""

"""Match

# syntax
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
"""

txt = "I love to teach python and javaScript"
match = re.match(
    "I love to teach", txt, re.I
)  # It returns an object with span, and match
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

span = (
    match.span()
)  # We can get the starting and ending position of the match as tuple using span
print(span)  # (0, 15)

start, end = span
print(start, end)  # 0 15

substring = txt[start:end]
print(substring)  # I love to teach

"""As you can see from the example above, the pattern we are looking for (or the substring we are looking for) is I love to teach. The match function returns an object only if the text starts with the pattern."""

txt = "I love to teach python and javaScript"
match = re.match("I like to teach", txt, re.I)
print(match)  # None

"""The string does not match with I like to teach, therefore there was no match and the match method returned None."""


"""Search

# syntax
re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag"""

txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

match = re.search("first", txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>

span = match.span()
print(span)  # (100, 105)

start, end = span
print(start, end)

substring = txt[start:end]
print(substring)  # first

"""As you can see, search is much better than match because it can look for the pattern throughout the text. Search returns a match object with a first match that was found, otherwise it returns None. A much better re function is findall. This function checks for the pattern through the whole string and returns all the matches as a list."""

"""Searching for All Matches Using findall

findall() returns all the matches as a list"""

txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

matches = re.findall("python", txt, re.I)
print(matches)  # ['Python', 'python']

matches = re.findall("language", txt, re.I)
print(matches)

"""Since we are using re.I both lowercase and uppercase letters are included. If we do not have the re.I flag, then we will have to write our pattern differently. Let us check it out:"""

txt = """Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language"""

matches = re.findall("Python|python", txt)
print(matches)

matches = re.findall("[Pp]ython", txt)
print(matches)  # ['Python', 'python']

"""Let us add one more example. The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text."""

txt = """%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?"""

replace = re.sub("%", "", txt)
print(replace)

"""Splitting Text Using RegEx Split"""

txt = """I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?"""

split = re.split("\n", txt)  # splitting using \n - end of line symbol
print(split)

"""Writing RegEx Patterns

To declare a string variable we use a single or double quote. To declare RegEx variable r''. The following pattern only identifies apple with lowercase, to make it case insensitive either we should rewrite our pattern or we should add a flag."""

regex_patters = r"apple"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(regex_patters, txt)
print(matches)
matches = re.findall(regex_patters, txt, re.I)
print(matches)

"""
[]: A set of characters
[a-c] means, a or b or c
[a-z] means, any letter from a to z
[A-Z] means, any character from A to Z
[0-3] means, 0 or 1 or 2 or 3
[0-9] means any number from 0 to 9
[A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
\: uses to escape special characters
\d means: match where the string contains digits (numbers from 0-9)
\D means: match where the string does not contain digits
. : any character except new line character(\n)
^: starts with
r'^substring' eg r'^love', a sentence that starts with a word love
r'[^abc] means not a, not b, not c.
$: ends with
r'substring$' eg r'love$', sentence that ends with a word love
*: zero or more times
r'[a]*' means a optional or it can occur many times.
+: one or more times
r'[a]+' means at least once (or more)
?: zero or one time
r'[a]?' means zero times or once
{3}: Exactly 3 characters
{3,}: At least 3 characters
{3,8}: 3 to 8 characters
|: Either or
r'apple|banana' means either apple or a banana
(): Capture and group"""


"""Square Bracket

Let us use square bracket to include lower and upper case"""

pattern = r"[Aa]pple"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(pattern, txt)
print(matches)

"""If we want to look for the banana, we write the pattern as follows:

"""

pattern = r"[Aa]pple|[Bb]anana"
txt = "Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away."
matches = re.findall(pattern, txt)
print(matches)

"""Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana."""

"""Escape character(\) in RegEx"""

pattern = r"\d"  # d is a special character which means digits
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(pattern, txt)
print(matches)

"""One or more times(+)"""

pattern = (
    r"\d+"  # d is a special character which means digits, + mean one or more times
)
txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
matches = re.findall(pattern, txt)
print(matches)

"""Period(.)"""

pattern = (
    r"[a]."  # this square bracket means a and . means any character except new line
)
txt = """Apple and banana are fruits"""
matches = re.findall(pattern, txt)
print(matches)

pattern = r"[a].+"  # . any character, + any character one or more times
matches = re.findall(pattern, txt)
print(matches)

"""Zero or more times(*)

Zero or many times. The pattern could may not occur or it can occur many times."""

pattern = r"[b].*"  # . any character, * any character zero or more times
txt = """Apple and banana are fruits"""
matches = re.findall(pattern, txt)
print(matches)

"""Zero or one time(?)

Zero or one time. The pattern may not occur or it may occur once."""

txt = """I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail."""

pattern = r"[Ee]-?mail"  # ? means here that '-' is optional
matches = re.findall(pattern, txt)
print(matches)

"""Quantifier in RegEx

We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:"""

txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
pattern = r"\d{4}"
matches = re.findall(pattern, txt)
print(matches)

rex_pattern = r"\d{1,4}"
matches = re.findall(rex_pattern, txt)
print(matches)

"""Cart ^

Starts with"""

txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
pattern = r"^This"  # ^ means starts with
matches = re.findall(pattern, txt)
print(matches)

"""Negation"""

txt = "This regular expression example was made on December 6,  2019 and revised on July 8, 2021"
pattern = r"[^A-Za-z ]+"  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(pattern, txt)
print(matches)
