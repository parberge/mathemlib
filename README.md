# Currently not working
Since there is no restful api from mathem, this will probably require way to much work.
For instance, the example below stopped working just a few days after committing the code.
Right now I'm not spending time on developing this....

# mathemlib
A python lib for interacting with mathem.se

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

# Print info about the order
print(my_mathem.get_info(order_id=order[0]))
{'Status': 'Bekräftad', 'Order date': '2017-05-11', 'Delivery date': '17-maj-2017 kl 17:00 - 19:00'}
```
