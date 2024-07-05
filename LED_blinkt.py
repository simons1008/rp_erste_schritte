# LED blinkt

# Bibliotheken importieren
from gpiozero import LED
from time import sleep

# LED Pin definieren
led = LED(17)

# Loop
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)