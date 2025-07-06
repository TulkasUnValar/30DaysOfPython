"""Python datetime

Python has got datetime module to handle date and time."""

import datetime

print(dir(datetime))
"""['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

"""With dir or help built-in commands it is possible to know the available functions in a certain module. As you can see, in the datetime module there are many functions, but we will focus on date, datetime, time and timedelta. Let se see them one by one."""

"""Getting datetime Information"""

from datetime import datetime

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond
timestamp = now.timestamp()
print(day, month, year, hour, minute, second, microsecond)
print("timestamp: ", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}")

"""Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC."""

"""Formatting Date Output Using strftime"""

new_year = datetime(2025, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
microsecond = new_year.microsecond
print(day, month, year, hour, minute, second, microsecond)
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}")

"""Formatting date time using strftime method and the documentation can be found here: https://strftime.org/."""

# Current time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print(f"time: {t}")

# mm/dd/YY H:M:S format
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Time one: {time_one}")

# dd/mm/YY H:M:S format
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Time two: {time_two}")


"""
Here are all the strftime symbols we use to format time. An example of all the formats for this module.

Python strftime cheatsheet
🐍🐍🐍
Code	Example	        Description
%a	  Sun	            Weekday as locale’s abbreviated name.
%A	  Sunday	        Weekday as locale’s full name.
%w	  0	              Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
%d	  08	            Day of the month as a zero-padded decimal number.
%-d	  8	              Day of the month as a decimal number. (Platform specific)
%b	  Sep	            Month as locale’s abbreviated name.
%B	  September	      Month as locale’s full name.
%m	  09	            Month as a zero-padded decimal number.
%-m	  9             	Month as a decimal number. (Platform specific)
%y	  13	            Year without century as a zero-padded decimal number.
%Y	  2013	          Year with century as a decimal number.
%H	  07	            Hour (24-hour clock) as a zero-padded decimal number.
%-H	  7	              Hour (24-hour clock) as a decimal number. (Platform specific)
%I	  07	            Hour (12-hour clock) as a zero-padded decimal number.
%-I	  7	              Hour (12-hour clock) as a decimal number. (Platform specific)
%p	  AM	            Locale’s equivalent of either AM or PM.
%M	  06	            Minute as a zero-padded decimal number.
%-M	  6	              Minute as a decimal number. (Platform specific)
%S	  05	            Second as a zero-padded decimal number.
%-S	  5	              Second as a decimal number. (Platform specific)
%f	  000000	        Microsecond as a decimal number, zero-padded to 6 digits.
%z	  +0000	          UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
%Z	  UTC             Time zone name (empty string if the object is naive).
%j	  251	            Day of the year as a zero-padded decimal number.
%-j	  251	            Day of the year as a decimal number. (Platform specific)
%U	  36	            Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year    preceding the first Sunday are considered to be in week 0.
%-U	  36	            Week number of the year (Sunday as the first day of the week) as a decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. (Platform specific)
%W	  35	            Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.
%-W	  35	            Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0. (Platform specific)
%c	  Sun           Sep 8 07:06:05 2013	Locale’s appropriate date and time representation.
%x	  09/08/13	    Locale’s appropriate date representation.
%X	  07:06:05	    Locale’s appropriate time representation.
%%	  %	            A literal '%' character.

Platform-specific directives
The full set of format codes supported varies across platforms, because Python calls the platform C library's strftime() function, and platform variations are common. To see the full set of format codes supported on your platform, consult the strftime(3) documentation: https://man7.org/linux/man-pages/man3/strftime.3.html.

The Python docs contain all the format codes that the C standard (1989 version) requires, and these work on all platforms with a standard C implementation. Note that the 1999 version of the C standard added additional format codes. These include codes for non-zero-padded numbers, that can be obtained by appending a dash (-) (UNIX) or hash (#) (Windows) after the percent (%) sign.

Source

This cheatsheet was built from the Python standard library strftime documentation: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes. See github.com/mccutchen/strftime.org for the build source code.

See also

You might also like PyFormat.info or the interactive strfti.me."""


"""Basic formatting
Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.

Since the elements are not represented by something as descriptive as a name this simple style should only be used to format a relatively small number of elements.

Old
'%s %s' % ('one', 'two')
New
'{} {}'.format('one', 'two')
Output
one two
Old
'%d %d' % (1, 2)
New
'{} {}'.format(1, 2)
Output
1 2
With new style formatting it is possible (and in Python 2.6 even mandatory) to give placeholders an explicit positional index.

This allows for re-arranging the order of display without changing the arguments.

This operation is not available with old-style formatting.

New
'{1} {0}'.format('one', 'two')
Output
two one
Value conversion
The new-style simple formatter calls by default the __format__() method of an object for its representation. If you just want to render the output of str(...) or repr(...) you can use the !s or !r conversion flags.

In %-style you usually use %s for the string representation but there is %r for a repr(...) conversion.

Setup
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'
Old
'%s %r' % (Data(), Data())
New
'{0!s} {0!r}'.format(Data())
Output
str repr
In Python 3 there exists an additional conversion flag that uses the output of repr(...) but uses ascii(...) instead.

Setup
class Data(object):

    def __repr__(self):
        return 'räpr'
Old
'%r %a' % (Data(), Data())
New
'{0!r} {0!a}'.format(Data())
Output
räpr r\xe4pr
Padding and aligning strings
By default values are formatted to take up only as many characters as needed to represent the content. It is however also possible to define that a value should be padded to a specific length.

Unfortunately the default alignment differs between old and new style formatting. The old style defaults to right aligned while for new style it's left.

Align right:

Old
'%10s' % ('test',)
New
'{:>10}'.format('test')
Output
      test
Align left:

Old
'%-10s' % ('test',)
New
'{:10}'.format('test')
Output
test      
Again, new style formatting surpasses the old variant by providing more control over how values are padded and aligned.

You are able to choose the padding character:

This operation is not available with old-style formatting.

New
'{:_<10}'.format('test')
Output
test______
And also center align values:

This operation is not available with old-style formatting.

New
'{:^10}'.format('test')
Output
   test   
When using center alignment where the length of the string leads to an uneven split of the padding characters the extra character will be placed on the right side:

This operation is not available with old-style formatting.

New
'{:^6}'.format('zip')
Output
 zip  
Truncating long strings
Inverse to padding it is also possible to truncate overly long values to a specific number of characters.

The number behind a . in the format specifies the precision of the output. For strings that means that the output is truncated to the specified length. In our example this would be 5 characters.

Old
'%.5s' % ('xylophone',)
New
'{:.5}'.format('xylophone')
Output
xylop
Combining truncating and padding
It is also possible to combine truncating and padding:

Old
'%-10.5s' % ('xylophone',)
New
'{:10.5}'.format('xylophone')
Output
xylop     
Numbers
Of course it is also possible to format numbers.

Integers:

Old
'%d' % (42,)
New
'{:d}'.format(42)
Output
42
Floats:

Old
'%f' % (3.141592653589793,)
New
'{:f}'.format(3.141592653589793)
Output
3.141593
Padding numbers
Similar to strings numbers can also be constrained to a specific width.

Old
'%4d' % (42,)
New
'{:4d}'.format(42)
Output
  42
Again similar to truncating strings the precision for floating point numbers limits the number of positions after the decimal point.

For floating points the padding value represents the length of the complete output. In the example below we want our output to have at least 6 characters with 2 after the decimal point.

Old
'%06.2f' % (3.141592653589793,)
New
'{:06.2f}'.format(3.141592653589793)
Output
003.14
For integer values providing a precision doesn't make much sense and is actually forbidden in the new style (it will result in a ValueError).

Old
'%04d' % (42,)
New
'{:04d}'.format(42)
Output
0042
Signed numbers
By default only negative numbers are prefixed with a sign. This can be changed of course.

Old
'%+d' % (42,)
New
'{:+d}'.format(42)
Output
+42
Use a space character to indicate that negative numbers should be prefixed with a minus symbol and a leading space should be used for positive ones.

Old
'% d' % ((- 23),)
New
'{: d}'.format((- 23))
Output
-23
Old
'% d' % (42,)
New
'{: d}'.format(42)
Output
 42
New style formatting is also able to control the position of the sign symbol relative to the padding.

This operation is not available with old-style formatting.

New
'{:=5d}'.format((- 23))
Output
-  23
New
'{:=+5d}'.format(23)
Output
+  23
Named placeholders
Both formatting styles support named placeholders.

Setup
data = {'first': 'Hodor', 'last': 'Hodor!'}
Old
'%(first)s %(last)s' % data
New
'{first} {last}'.format(**data)
Output
Hodor Hodor!
.format() also accepts keyword arguments.

This operation is not available with old-style formatting.

New
'{first} {last}'.format(first='Hodor', last='Hodor!')
Output
Hodor Hodor!
Getitem and Getattr
New style formatting allows even greater flexibility in accessing nested data structures.

It supports accessing containers that support __getitem__ like for example dictionaries and lists:

This operation is not available with old-style formatting.

Setup
person = {'first': 'Jean-Luc', 'last': 'Picard'}
New
'{p[first]} {p[last]}'.format(p=person)
Output
Jean-Luc Picard
Setup
data = [4, 8, 15, 16, 23, 42]
New
'{d[4]} {d[5]}'.format(d=data)
Output
23 42
As well as accessing attributes on objects via getattr():

This operation is not available with old-style formatting.

Setup
class Plant(object):
    type = 'tree'
New
'{p.type}'.format(p=Plant())
Output
tree
Both type of access can be freely mixed and arbitrarily nested:

This operation is not available with old-style formatting.

Setup
class Plant(object):
    type = 'tree'
    kinds = [{'name': 'oak'}, {'name': 'maple'}]
New
'{p.type}: {p.kinds[0][name]}'.format(p=Plant())
Output
tree: oak
Datetime
New style formatting also allows objects to control their own rendering. This for example allows datetime objects to be formatted inline:

This operation is not available with old-style formatting.

Setup
from datetime import datetime
New
'{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5))
Output
2001-02-03 04:05
Parametrized formats
Additionally, new style formatting allows all of the components of the format to be specified dynamically using parametrization. Parametrized formats are nested expressions in braces that can appear anywhere in the parent format after the colon.

Old style formatting also supports some parametrization but is much more limited. Namely it only allows parametrization of the width and precision of the output.

Parametrized alignment and width:

This operation is not available with old-style formatting.

New
'{:{align}{width}}'.format('test', align='^', width='10')
Output
   test   
Parametrized precision:

Old
'%.*s = %.*f' % (3, 'Gibberish', 3, 2.7182)
New
'{:.{prec}} = {:.{prec}f}'.format('Gibberish', 2.7182, prec=3)
Output
Gib = 2.718
Width and precision:

Old
'%*.*f' % (5, 2, 2.7182)
New
'{:{width}.{prec}f}'.format(2.7182, width=5, prec=2)
Output
 2.72
The nested format can be used to replace any part of the format spec, so the precision example above could be rewritten as:

This operation is not available with old-style formatting.

New
'{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.3')
Output
Gib = 2.72
The components of a date-time can be set separately:

This operation is not available with old-style formatting.

Setup
from datetime import datetime
dt = datetime(2001, 2, 3, 4, 5)
New
'{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M')
Output
2001-02-03 04:05
The nested formats can be positional arguments. Position depends on the order of the opening curly braces:

This operation is not available with old-style formatting.

New
'{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3)
Output
     +2.72
And of course keyword arguments can be added to the mix as before:

This operation is not available with old-style formatting.

New
'{:{}{sign}{}.{}}'.format(2.7182818284, '>', 10, 3, sign='+')
Output
     +2.72
Custom objects
The datetime example works through the use of the __format__() magic method. You can define custom format handling in your own objects by overriding this method. This gives you complete control over the format syntax used.

This operation is not available with old-style formatting.

Setup
class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'
New
'{:open-the-pod-bay-doors}'.format(HAL9000())
Output
I'm afraid I can't do that."""

date_string = "5 december 2025"
print(f"date_string = {date_string}")

date_object = datetime.strptime(date_string, "%d %B %Y")
print(f"date_object = {date_object}")

print(
    f"date_object.strftime('%A, %B %d, %Y') = {date_object.strftime('%A, %B %d, %Y')}"
)


"""Using date from datetime"""

from datetime import date

d = date(2025, 1, 1)
print(d)

print(f"Current date: {d.today()}")

# date object of today's date

today = date.today()

print(f"Current year: {today.year}")
print(f"Current month: {today.month}")
print(f"Current day: {today.day}")

time_one = today.strftime("%d/%m/%Y, %H:%M:%S")
print(f"Current date and time: {time_one}")


"""Time Objects to Represent Time"""

from datetime import time

# time(hour = 0, minute = 0, second = 0)
t = time()
print(f"t = {t}")

# time(hour, minute and second)
a = time(10, 30, 50)
print(f"a = {a}")

# time(hour, minute and second)
b = time(hour=8, minute=53, second=50)
print(f"b = {b}")

# time(hour, minute, second, microsecond)
c = time(10, 30, 50, 100000)
print(f"c = {c}")


"""Difference Between Two Points in Time Using"""

today = date(year=2025, month=7, day=5)
new_year = date(year=2026, month=1, day=1)
time_difference = new_year - today
print(f"Time difference = {time_difference}")

t1 = datetime(year=2025, month=7, day=5, hour=9, minute=1, second=50)
t2 = datetime(year=2026, month=1, day=1, hour=00, minute=00, second=1)
time_difference = t2 - t1
print(f"Time difference = {time_difference}")


"""Difference Between Two Points in Time Using timedelta"""

from datetime import timedelta

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
difference = t1 - t2
print(f"t3 = {difference}")
