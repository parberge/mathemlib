# mathemlib
A python lib for interacting with mathem.se

Not much functionality at the moment. Stay tuned

# Simple example
```
from mathemlib import Mathem

my_mathem = Mathem(config_file='my_mathem_config.yaml')
my_mathem.login()

order = my_mathem.get_orders(limit=1)
print(my_mathem.get_info(order_id=order[0]))
```