import re

# Your task is to write a regular expression (regex) that will match a string only if it contains at least one valid
# date, in the format [mm-dd] (that is, a two-digit month, followed by a dash, followed by a two-digit date, surrounded
# by square brackets).
# You should assume the year in question is not a leap year. Therefore, the number of days each month should have are as
# follows:
# 1. January - 31 days
# 2. February - 28 days (leap years are ignored)
# 3. March - 31 days
# 4. April - 30 days
# 5. May - 31 days
# 6. June - 30 days
# 7. July - 31 days
# 8. August - 31 days
# 9. September - 30 days
# 10. October - 31 days
# 11. November - 30 days
# 12. December - 31 days
# All text outside a valid date can be ignored, including other invalid dates.
#
# For example:
# "[01-23]" // January 23rd is a valid date
# "[02-31]" // February 31st is an invalid date
# "[02-16]" // valid
# "[ 6-03]" // invalid format
# "ignored [08-11] ignored" // valid
# "[3] [12-04] [09-tenth]" // December 4th is a valid date
# test.describe("Basic tests")
# test.expect(valid_date.search("[01-23]")!=None, "January 23rd is a valid date")
# test.expect(valid_date.search("[02-31]")==None, "February 31st is an invalid date")
# test.expect(valid_date.search("[02-16]")!=None , "valid")
# test.expect(valid_date.search("[ 6-03]")==None, "invalid format")
# test.expect(valid_date.search("ignored [08-11] ignored")!=None, "valid")
# test.expect(valid_date.search("[3] [12-04] [09-tenth]")!=None, "December 4th is a valid date")
# test.expect(valid_date.search("[02-00]")==None, "invalid format")
# test.expect(valid_date.search("[[[08-29]]]")!=None, "valid")
# test.expect(valid_date.search("[13-02]")==None, "invalid format")
# test.expect(valid_date.search("[02-[08-11]04]")!=None, "valid")
# [mm-dd]
month_31 = ['01', '03', '05', '07', '08', '10', '12']
month_30 = ['04', '06', '09', '11']


def valid_date(date):
    date_regex = re.compile(r'''
    \[((02-((0[1-9])|(1\d)|(2[0-8])))| # February
    (((0[13578])|(1[02]))-((0[1-9])|([12]\d)|(3[01])))| # month group 31 days
    (((0[469])|(11))-((0[1-9])|([12]\d)|(30))))\]  # month group 30 days
    ''', re.VERBOSE)
    match_object = date_regex.search(date)
    if match_object is not None:
        return match_object.group()
    else:
        return None


text = '[03-11]'
print(valid_date(text))
valid_date = re.compile(r'\[((02-((0[1-9])|(1\d)|(2[0-8])))|(((0[13578])|(1[02]))-((0[1-9])|([12]\d)|(3[01])))|(((0[469])|(11))-((0[1-9])|([12]\d)|(30))))\]')
r'\[((0\d)|(1[012]))-([0-3]\d)\]'
