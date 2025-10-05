# Read block data from Arduino, write block data to Arduino
# Quelle: https://forums.raspberrypi.com/viewtopic.php?t=203286
# Ignore input/output error using Python module SMBus
# Quelle: https://stackoverflow.com/questions/15245235/input-output-error-using-python-module-smbus-a-raspberry-pi-and-an-arduino

from time import sleep
import smbus
import subprocess
bus = smbus.SMBus(1)
address = 0x08
raspi_data = [240, 244, 250, 254]

# Give the I2C device time to settle
sleep(2)

# Zyklen
cycles = 100

# Error counter
error = 0

for i in range(cycles):
    try:
        arduino_data = bus.read_i2c_block_data(address, 99, 4)
        print(arduino_data)
    except IOError:
        print("Error during bus.read_i2c_block_data()")
        error += 1
    sleep(0.5)
    
    try:
        raspi_data[3] += 1
        raspi_data[0] += 1
        bus.write_i2c_block_data(address, 98, raspi_data)
    except IOError:
        print("Error during bus.write_i2c_block_data()")
        error += 1
    sleep(0.5)

print("\n", cycles, "Zyklen durchlaufen,", error, "mal IOError") 