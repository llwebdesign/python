# login_server.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class LoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        html = """
        <html>
        <head>
            <title>Login</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #6a11cb, #2575fc);
                    height: 100vh;
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
                .container {
                    background-color: white;
                    padding: 30px;
                    border-radius: 12px;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
                    width: 300px;
                    text-align: center;
                }
                h2 {
                    color: #333;
                    margin-bottom: 20px;
                }
                input[type="text"], input[type="password"] {
                    width: 90%;
                    padding: 10px;
                    margin: 8px 0;
                    border: 1px solid #ccc;
                    border-radius: 6px;
                }
                button {
                    width: 100%;
                    padding: 10px;
                    background-color: #2575fc;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    font-weight: bold;
                }
                button:hover {
                    background-color: #1b5edb;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Login</h2>
                <form method="POST" action="/">
                    <input type="text" name="username" placeholder="Benutzername" required><br>
                    <input type="password" name="password" placeholder="Passwort" required><br>
                    <button type="submit">Einloggen</button>
                </form>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length).decode("utf-8")
        data = parse_qs(body)
        username = data.get("username", [""])[0]
        password = data.get("password", [""])[0]

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        if username == "admin" and password == "1234":
            message = f"<h1>Willkommen, {username}!</h1>"
        else:
            message = "<h1>Falsche Login-Daten!</h1><a href='/'>Zurück</a>"

        self.wfile.write(message.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), LoginHandler)
    print("Server läuft auf http://localhost:8080")
    server.serve_forever()
