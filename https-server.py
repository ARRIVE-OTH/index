# Python-Server wurde mit ChatGPT, am 09.12.2025, GPT5 erstellt
import http.server
import ssl

server_address = ('0.0.0.0', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS Server läuft auf https://localhost:4443")
httpd.serve_forever()

