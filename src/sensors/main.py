#!/usr/bin/python
readcount = 0
from i2c import AtlasI2C

addr1 = 97
addr2 = 99
addr3 = 100
delaytime = 6
readcount = 0

atlas = AtlasI2C()
atlas.address(addr1)
print('address 1 = ',addr1)
atlas.poll(delaytime)
atlas.address(addr2)
print('address 2 = ',addr2)
atlas.poll(delaytime)
atlas.address(addr3)
print('address 3 = ',addr3)
atlas.poll(delaytime)

	
