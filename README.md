# mathemlib
A python library for https://www.mathem.se  
Not much functionality at the moment. Stay tuned

# Simple example
```
from mathemlib import Mathem

my_mathem = Mathem()
my_mathem.user = 'my username'
my_mathem.password = 'my password'
my_mathem.login()

# Only care for one order (which should be the latest)
order = my_mathem.get_orders(limit=1)

print(order)
```
Will output something like:
```
{u'20316076': {}}
```
Not very useful, but it's a start
