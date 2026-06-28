# given the last 2 digits of a year, return whetherthat year is valid. A year is valid
# it is either 50 years in the past or 10 years in the future. Given the year
# for example if it is 50 is invalid because 1950 or 2050 are not valid.

from datetime import date

globalYear = 0

def GetYearTest(twoDigitYear, year):
    curYear = globalYear
    lower = (curYear - 50) % 100
    upper = curYear % 100
    chopped = curYear % 100
    top2 = int(curYear // 100) * 100
    if lower > upper:
        print(f"checking not within the bounds from {upper} to {lower}")
        # if its not within the range from 26 to 76 then it is valid
        if not (upper < twoDigitYear < lower):
            if twoDigitYear > chopped:
                print((top2 - 100) + twoDigitYear)
                return (top2 - 100) + twoDigitYear
            else:
                print(top2 + twoDigitYear)
                return top2 + twoDigitYear
    else:
        if lower <= twoDigitYear <= upper:
            print(top2 + twoDigitYear)
            return top2 + twoDigitYear
    lower = curYear % 100
    upper = (curYear + 10) % 100

    if lower > upper:
        print(f"checking within the bounds from {lower} to {upper + 100}")
        # if its not within the range from 26 to 76 then it is valid
        if not (upper <= twoDigitYear <= lower):
            # 2096
            # 96
            # 03
            if twoDigitYear < chopped:
                print((top2 + 100) + twoDigitYear)
                return (top2 + 100) + twoDigitYear
            else:
                print(top2 + twoDigitYear)
                return top2 + twoDigitYear
    else:
        # normal
        print(f"checking within the bounds from {lower} to {upper}")
        if lower <= twoDigitYear <= upper:
            print(top2 + twoDigitYear)
            return top2 + twoDigitYear

    print(-1)

def GetYear(twoDigitYear):
    GetYearTest(twoDigitYear)

yearTests = [2036, 3077]

globalYear = yearTests[0]
reze = GetYear(90)
assert reze == 1990
globalYear = yearTests[1]
reze = GetYear(79)
assert reze == 3079


year = 90
globalYear = 2026
GetYear(year)

# 2026
#

# curYear


GetYear(76)
