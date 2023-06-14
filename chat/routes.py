from flask import session, redirect, url_for, render_template, request, Blueprint, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS


main = Blueprint('main', __name__)
cors = CORS(main, resources={r"/*": {"origins": "*"}})
# socketio = SocketIO(main)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['room'] = request.form['room']
        return redirect(url_for('main.chat'))
    return render_template('index.html')


@main.route('/chat')
def chat():
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('chat.html', name=name, room=room)


@main.route('/dynamic-url', methods=['GET'])
def dynamic_url():

    return {'url': url}

