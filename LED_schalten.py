# LED_schalten

# Bibliotheken importieren
from gpiozero import LED, Button
from time import sleep

# LED Pin und Button Pin definieren
led = LED(17)
button = Button(27)

# Loop
while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5)