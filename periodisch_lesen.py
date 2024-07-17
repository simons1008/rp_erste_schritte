# Datei periodisch öffnen - lesen - schließen

# Bibliotheken importieren
import os
import time
from filelock import FileLock

# Log-Datei löschen
os.remove("log_Datei.txt")

# Dateien definieren
file_path = "meine_Datei.txt"
lock_path = "meine_Datei.txt.lock"

# Periode definieren (in Sekunden)
PERIODE = 10

# Loop
for i in range(10):
    # lock
    lock = FileLock(lock_path, timeout=1)

    # Input-Datei öffnen, lesen und schließen
    with lock:
        with open(file_path, mode="r", encoding="utf-8") as datei:
            mein_text = datei.read()
    
    # Output-Datei öffnen, mein_text anhängen
    with open("log_Datei.txt", mode="a", encoding="utf-8") as datei:
        datei.write(mein_text + "\n")
    
    # schlafen
    time.sleep(PERIODE)
    