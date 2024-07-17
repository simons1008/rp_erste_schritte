# Datei periodisch öffnen - schreiben - schließen

# Bibliothekem importieren
import time
from filelock import FileLock

# Dateien definieren
file_path = "meine_Datei.txt"
lock_path = "meine_Datei.txt.lock"

# Periode definieren (in Sekunden)
PERIODE = 1

# Loop
for i in range(100):
    # aktuelle Zeit lesen
    zeitString = time.localtime()

    # yyyy-mm-dd hh:mm:ss erzeugen
    datum_zeit_text = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        zeitString[0], zeitString[1], zeitString[2],
        zeitString[3], zeitString[4], zeitString[5])

    # datum_zeit_text auf die Konsole schreiben
    print(datum_zeit_text)
        
    # lock
    lock = FileLock(lock_path, timeout=1)

    # Output-Datei öffnen, schreiben und schließen
    with lock:
        with open(file_path, mode="w", encoding="utf-8") as datei:
            datei.write(datum_zeit_text)
    
    # schlafen
    time.sleep(PERIODE)         
