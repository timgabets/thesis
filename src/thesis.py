#!/usr/bin/python
import time
from sp500 import sp_500
from portfolio import portfolio

sp500 = sp_500()

p = portfolio(sp500.random(5), '2013-01-01', '2015-01-01', 0)
start_time = time.time()
p.calc()
print("--- %s seconds ---" % (time.time() - start_time))

print "\nRisky portfolio:"
r = portfolio(p.get_risky()[0], '2015-01-01', '2016-01-01', None, p.get_risky()[1])

print "\nConservative portfolio:"
c = portfolio(p.get_conservative()[0], '2015-01-01', '2016-01-01', None, p.get_conservative()[1])
