import socket
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 8000
    try:
        server = ThreadingHTTPServer((host, port), QuietHandler)
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f"StudyDock is running at http://{local_ip}:{port}")
        print("Open this on another laptop using the same Wi‑Fi network.")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            server.server_close()
    except OSError as exc:
        print(f"Could not start server: {exc}")
        print("Try a different port or make sure no other app is using 8000.")
