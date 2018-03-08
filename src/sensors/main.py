from i2c import AtlasI2C

addr1 = 97
addr2 = 99
addr3 = 100

delaytime = 6

def main():
	while True:
		atlas = AtlasI2C()
		atlas.address(addr1)
		atlas.poll(delaytime)
		atlas.address(addr2)
		atlas.poll(delaytime)
		atlas.address(addr3)
		atlas.poll(delaytime)

	
