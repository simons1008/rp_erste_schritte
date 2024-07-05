# SolarCar Instrumentation Demo - Kontrolle durch Eingabefeld
# Das Fenster soll ein Gitter 3 Zeilen und 5 Spalten aufweisen

# Bibliothek importieren
import tkinter as tk

# Konstante
MAX_SPEED = 50

# Modul für die GUI Erstellung importieren
root = tk.Tk()
root.title("Car Instrumentation Demo")

# Gitter konfigurieren
# Zeilen
for i in range(3):
    root.rowconfigure(i, minsize=150)
# Spalten
for i in range(5):
    root.columnconfigure(i, minsize=150)

# Funktion zur Umrechnung von Prozent in Geschwindigkeit
def prozent_in_geschwindigkeit(event):
    prozent = int(eingabefeld_wert.get())
    # umrechnen
    geschwindigkeit = MAX_SPEED * prozent * 0.01
    # Steuervariable setzen
    ausgabefeld_wert.set(geschwindigkeit)

# Funktion zum Schließen des Fensters
def close_window():
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

# Steuervariable für das Eingabefeld erzeugen
eingabefeld_wert = tk.StringVar()

# Eingabefeld erzeugen und in GUI Elemente einbetten
eingabefeld = tk.Entry(root, textvariable=eingabefeld_wert, width=3, font = ("arial", 20))
eingabefeld.grid(row=0, column=2)

# Kommentarfeld erzeugen und in GUI Elemente einbetten
kommentar0 = tk.Label(root, text="Prozent", width=7, font = ("arial", 20))
kommentar0.grid(row=0, column=3, sticky = tk.W)

# Taste "Return" ruft die Funktion prozent_in_geschwindigkeit auf
eingabefeld.bind('<Key-Return>', prozent_in_geschwindigkeit)

# Schaltfläche erzeugen und in GUI Elemente einbetten
schaltflaeche = tk.Button(root, text="Exit", bg="orange", font = ("arial, 20"), command = close_window)
schaltflaeche.grid(row=2, column=4)

# Hauptschleife, damit die GUI angezeigt wird
root.mainloop()