"""
Regular expression basics:
. Any character (except new line)
a The character a
ab The string ab
a|b a or b
a* Zero or more of a
a+ One or more of a
\ Escapes special character

Regular expression quantifiers:
* 0 or more
+ 1 or more
? 0 or 1
{3} Exactly 3
{3,} At least 3
{3,8} 3 to 8

Regular expressions groups:
(...) Capturing group
(?...) Non-capturing group
\Y Matches the Y´th captured group

Regular expressions character classes:
[ab-d] Other characters between a and d
[^ab-d] Other characters not between a and d
[\b] Backspace character
\d One digit
\D Not a digit
\s One whitespace character
\S Not a whitespace character
\w One word character
\W One non a word character

Regular expression assertions:
^ Start of line
$ End of line
\b Word boundary
\B Non-word boundary
(?=...) Positive lookahead
(?!...) Negative lookahead

Regular expressions flags:
g Global match
i Ignore case 
m ^and$ match at the beginning and end of each line  


Regular expressions special characters:
\n Newline
\t Tab
\f Formfeed
\r Carriage return
\YYY Octal character YYY
\xHH Hexadecimal character HH
\uYYYY Hexadecimal character YYYY
\cY Control character Y

Regular expressions replacement:
$$ inserts $
$& inserts entire match
$` inserts text before match
$' inserts text after match
$Y inserts captured group Y
"""