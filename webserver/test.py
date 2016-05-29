import stocks
import util
import alarm
import logger
import re
pattern_date = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
###
s = stocks.get_stocks()
assert(len(s)==4 or len(s) == 5)
for d in s:
    assert(type(d) == str and type(s[d]) == float)
    assert(pattern_date.match(d))
###

###

print '\nOK.'
