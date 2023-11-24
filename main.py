from flask import Flask, render_template

from flask_socketio import SocketIO
from flask_socketio import Namespace, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('home.html')


@socketio.on('message')
def handle_message(msg):
    print(msg)
    socketio.emit('message', msg)

if __name__ == '__main__':
    socketio.run(app, debug=True)
