from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Alive" #'<meta http-equiv="refresh" content="0; URL=https://Cybergirl.ittejas2004.repl.co"/>'


def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
