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

# url = None
# @main.route('/image', methods=['GET'])
# def image():
#     global url
#     url = request.args.get('url')
#     session['image_url'] = url
#     socketio.emit('image', {'image_url': session.get('image_url')}, broadcast=True, namespace='/test')
#     return jsonify({'status': 'success'})

@main.route('/dynamic-url', methods=['GET'])
def dynamic_url():

    return {'url': url}

# @socketio.on('connect')
# def handle_connect():
#     image_url = url  
#     emit('update_image', {'image_url': image_url}, broadcast=True)