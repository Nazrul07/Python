"""
A date in Python is not a data type of its own,
but we can import a module named datetime to work with dates as date objects.

"""
import datetime
x = datetime.datetime.now()
print(x)        # The date contains year, month, day, hour, minute, second, and microsecond


# Return the year and name of weekday
print(x.year)

"""
Some strftime -> string formate time

%Y	    Year (4 digits)	            2025
%y	    Year (2 digits)	            25
%m	    Month (01-12)           	11
%B	    Full month name	            November
%b	    Abbreviated month name     	Nov
%d	    Day of month	            04
%A	    Full weekday name	        Tuesday
%a	    Abbreviated weekday name	Tue
%H	    Hour (00-23)	            20
%I	    Hour (01-12)	            08
%p	    AM/PM	                    PM
%M	    Minute                  	43
%S	    Second	                    12
%U      Week number of year,        
        Sunday as the first         44
        day of week,
        00-53

%W      Week number of year,        45
        Monday as the first
        day of week, 00-53


%c      Local version of            Tue Nov  4 21:12:17 2025
        date and time

%x	    Local version of date	    12/31/18	
%X	    Local version of time       21:12:17

"""
print(x.strftime("Week Name: %A"), end = " ")
print(x.strftime("%a"))

print(x.strftime("Year: %Y"), end = " ")
print(x.strftime("%y"))

print(x.strftime("Month: %m"))

print(x.strftime("Month Name: %B"), end = " ")
print(x.strftime("%b"))

print(x.strftime("Day: %d"))

print(x.strftime("Hour: %H")) # 24H

print(x.strftime("Hour: %I")) # 12H

print(x.strftime("AM/PM: %p"))

print(x.strftime("Minute: %M")) 

print(x.strftime("Second: %S"))

print(x.strftime("Number of Weeks: %U"))


print(x.strftime("Local version of time and date: %c"))

print(x.strftime("Local version of date: %x"))

print(x.strftime("Local version of time: %X"))


"""
*****Creating Date Objects*****

To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

But we can add extra more - Hours, Minute, Seconds

"""

x = datetime.datetime(2020, 5, 17, 14, 30, 45)
print(x)