# schnurloser Taster
# Quelle: https://www.elektronik-kompendium.de/sites/raspberry-pi/2708141.htm
# Quelle für Raspberry Pi Zero angepasst an Raspberry Pi 4

# Deine ID: a582a564f60b38a3f62192d1db5e65f7
# Deine URL: http://elektronik.info/a582a564f60b38a3f62192d1db5e65f7
# Gültig bis: 04.07.2024 00:08

# Das Speichern von Werten erfolgt per HTTP-Request (GET-Methode). Die URL hat dabei folgenden Aufbau:
# http://elektronik.info/ID/DEVICE/VALUE

# Das Abrufen von Werten erfolgt per HTTP-Request (GET-Methode). Die URL hat dabei folgenden Aufbau:
# http://elektronik.info/ID/DEVICE

# Bibliotheken laden
# import machine
from gpiozero import LED, Button
# import network
import time
import requests

# WLAN-Konfiguration
# nicht notwendig bei Raspbian

# IoT-Webservice-Konfiguration
myID = 'a582a564f60b38a3f62192d1db5e65f7' # 32-stelliger Code
myDevice = 'IOT_88677' # oder selbst gewählter Name
# myString = 1 # Default-Wert
myString = 'Freund'

# Status-LED für die WLAN-Verbindung
# nicht notwendig bei Raspbian

# Funktion: WLAN-Verbindung
# nicht notwendig, wird von Raspbian gemacht

# Button initialisieren
# btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
btn = Button(27)
print()
print('Taster bereit')

# Funktion zur Taster-Auswertung
while True:
    time.sleep(0.1)
    if btn.is_pressed:
        print()
        try:
            if myString == 'Hallo': myString = 'Freund'
            elif myString == 'Freund': myString = 'Hallo'
            url = 'http://elektronik.info/' + myID + '/' + myDevice + '/' + str(myString)
            # HTTP-Request senden
            print('Request: GET', url)
            response = requests.get(url)
            if response.status_code == 200:
                print('Response:', response.content)
            else:
                print('Status-Code:', response.status_code)
                print('Fehler:', response.reason)
            response.close()
        except OSError:
            print('Fehler: Keine Verbindung')
        # Entprell-Pause
        time.sleep(0.1)