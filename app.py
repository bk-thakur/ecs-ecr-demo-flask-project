from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return f"<h1>Welcome to ECS Demo App 🚀</h1><p>Served from: {socket.gethostname()}</p>"

@app.route('/health')
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
