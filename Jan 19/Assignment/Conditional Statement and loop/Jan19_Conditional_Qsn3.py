"""
3. We add a Leap Day on February 29, almost every four years. The leap day is an extra, or
intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800,
1900, 2100, 2200, 2300 and 2500 are NOT leap years.
"""
leap_year = True
check_year = int(input("Enter a year to check: "))
if check_year % 4 == 0:
    if check_year % 100 == 0:
        if check_year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False
if bool(leap_year):
    print(f"The year {check_year} is a leap year.")
else:
    print(f"The year {check_year} is not a leap year.")
