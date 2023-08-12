import http.server
import socketserver
import webbrowser

IP = "127.0.0.1"
PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((IP, PORT), Handler)
try:
    root_dir = "index.html"  
    Handler.directory = root_dir
    Handler.cgi_directories = [root_dir]
    print(f"Serving at http://{IP}:{PORT}")
    webbrowser.open(f"http://{IP}:{PORT}")      
    httpd.serve_forever()

except KeyboardInterrupt:
    print("Server stopped.")