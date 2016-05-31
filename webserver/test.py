import stocks
import util
import alarm
import logger
import re
pattern_date = re.compile("^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
###
s = stocks.get_stocks()
for d in s:
    assert(type(d) == str and type(s[d]) == float)
    assert(pattern_date.match(d))
###
stats = (logger.Logger()).get_stats()
assert(type(stats) == dict)
assert(len(stats) == 2)
###

print '\nOK.'
