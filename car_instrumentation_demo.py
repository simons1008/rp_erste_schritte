# SolarCar Instrumentation Demo - Kontrolle durch Analogwert
# Das Fenster soll ein Gitter 3 Zeilen und 5 Spalten aufweisen

# Bibliotheken importieren
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import tkinter as tk

# Erzeuge den I2C Bus
i2c = busio.I2C(board.SCL, board.SDA)

# Erzeuge das Objekt das den I2C Bus benutzt
ads = ADS.ADS1115(i2c)

# Erzeuge einen single-ended input auf Kanal 0
chan = AnalogIn(ads, ADS.P0)

# Konstanten
MAX_SPEED = 50

# ID zum Beenden des .after Jobs
ID = "0"

# Konstruktor für das Fenster aufrufen
root = tk.Tk()
root.title("Car Instrumentation Demo")

# Gitter konfigurieren
# Zeilen
for i in range(3):
    root.rowconfigure(i, minsize=150)
# Spalten
for i in range(5):
    root.columnconfigure(i, minsize=150)

# Funktion zur Umrechnung von Analogwert in Geschwindigkeit
def analogwert_in_geschwindigkeit():
    global ID
    analogwert = chan.value
    # umrechnen
    geschwindigkeit = round(MAX_SPEED * analogwert/26000, 1)
    # Steuervariable setzen
    ausgabefeld_wert.set(str(geschwindigkeit))
    ID = root.after(500, analogwert_in_geschwindigkeit)

# Funktion zum Schließen des Fensters
def close_window():
    # .after Job beenden
    root.after_cancel(ID)
    # Fenster schließen
    root.destroy()

# Steuervariable für das Ausgabefeld erzeugen und initialisieren
ausgabefeld_wert = tk.StringVar()
ausgabefeld_wert.set("     ")

# Ausgabefeld erzeugen und in GUI Elemente einbetten
ausgabefeld = tk.Label(root, textvariable=ausgabefeld_wert, bg = "yellow", font = ("arial", 50))
ausgabefeld.grid(row=1, column=2)

# Kommentarfeld erzeugen und in GUI Elemente einbetten
kommentar1 = tk.Label(root, text="km/h", font = ("arial", 50))
kommentar1.grid(row=1, column=3)

# Schaltfläche erzeugen und in GUI Elemente einbetten
schaltflaeche = tk.Button(root, text="Exit", bg="orange", font = ("arial, 20"), command = close_window)
schaltflaeche.grid(row=2, column=4)

# Funktion zum ersten Mal aufrufen
analogwert_in_geschwindigkeit()

# auch beim Schließen des Fensters die Funktion aufrufen
root.protocol("WM_DELETE_WINDOW", close_window)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()