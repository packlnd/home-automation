import sys
sys.path.insert(0, '../')

import stocks
import util
import alarm
import logger

num_tests=4
passed_tests=0

#....

if num_tests == passed_tests:
    print 'OK.'
else:
    print 'Failed %d tests.' % (num_tests - passed_tests)
