# kleiner Webserver
# Quelle: https://u-labs.de/portal/3-wege-1-verbotener-um-programme-auf-dem-raspberry-pi-os-automatisch-zu-starten/
# Das Programm wird durch /home/ms/.config/autostart/autostart.desktop gestartet
# - Prüfe, ob das Programm läuft: ps -fC python
# - Wenn ja, kann es hier nicht nochmal gestartet werden!!

from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys, os

hostName = "0.0.0.0"
serverPort = 8080
webServer = None

class MyServer(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header("Content-Type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("Hallo vom Python Webserver", "utf-8"))

def terminate(signal,frame):
  webServer.server_close()
  sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, terminate)

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server gestartet: http://%s:%s mit pid %i" % (hostName, serverPort, os.getpid()))
    webServer.serve_forever()