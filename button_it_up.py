import time
import board
import digitalio

print("press the button!")

led = digitalio.DigitalInOut(board.D17)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D27)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    led.value = not button.value # light when button is pressed!