# mathemlib
A python lib for interacting with mathem.se

Not much functionality at the moment. Stay tuned

# Simple example
```
from mathemlib import Mathem

my_mathem = Mathem(config_file='my_mathem_config.yaml')
my_mathem.login()

# Only care for one order (which will be the latest)
order = my_mathem.get_orders(limit=1)

# Print info about the order
print(my_mathem.get_info(order_id=order[0]))
{'Status': 'Bekräftad', 'Order date': '2017-05-11', 'Delivery date': '17-maj-2017 kl 17:00 - 19:00'}
```