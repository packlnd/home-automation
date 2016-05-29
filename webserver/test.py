import stocks
import util
import alarm
import logger

###
s = stocks.get_stocks()
assert(len(s)==4)
for d in s:
    assert(type(d) == str and type(s[d]) == float)
###

###

print '\nOK.'
