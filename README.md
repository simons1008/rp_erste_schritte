# RP Erste Schritte

Meine ersten Schritte mit Raspberry Pi und OS Bookworm umfassen:

- Ansteuerung der GPIO Pins
- Installation von Adafruit Blinka
- Starten der virtuellen Umgegebung für die Bibliotheken, die auf Blinka aufsetzen
- Lesen der Analogwerte vom Analog-Digital-Converter ADS1115 über I2C
- einen kleinen Webserver, der in meinem lokalen Netz über localhost:8080 erreichbar ist
- die Datei autostart.desktop, die den Webserver beim Booten im Hintergrund startet
- einen schnurlosen Taster, der mit einem IoT Webservice zum Testen zusammenarbeitet
- GUI zur Darstellung der Analogwerte vom ADS1115
- Verbindung zum ThingsBoard Live Demo Server, Senden von Telemetrie-Daten, Empfang der "blinkingPeriod"
- FileLock beim konkurrierenden Zugriff auf eine Datei
