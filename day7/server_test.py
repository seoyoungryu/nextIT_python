import http.server
import socketserver
PORT = 8081
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",PORT), handler)
print('server start port:', PORT)
httpd.serve_forever()
# pip install flask