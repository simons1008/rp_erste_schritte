'''
i2c_v1.py
Simple Python 3 script to test I2C by alternately
sending a 1 and 0 over I2C every second and reading
back the response from the Arduino
Tested on Raspberry Pi 4 B+ and Adafruit Feather M0+
'''
# Quelle: https://community.element14.com/products/arduino/b/blog/posts/raspberry-pi-and-arduino-i2c-communication
# Geändert: i2cData wechselt zwischen 0 und 255
# Getestet mit Raspberry Pi 4 B und Arduino UNO R3

import smbus
import time
import sys
bus = smbus.SMBus(1)
address = 0x04              # Arduino I2C Address
def main():
    i2cData = False
    while 1:
        # send data
        i2cData = ~i2cData & 0xFF  # unsigned integer 
        bus.write_byte(address,i2cData)
        
        # request data
        print ("Arduino answer to RPi:", bus.read_byte(address))
        
        time.sleep(1)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: # ctrl-C
        sys.exit(0) 