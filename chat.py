from chat import create_app, socketio
from flask import session, redirect,  request, jsonify
app = create_app(debug=True)

@app.route('/image', methods=['GET'])
def image():
    url = request.args.get('url')
    session['url']=url
    socketio.emit('image', {'image_url': session['url']}, broadcast=True, namespace='/test')
 
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug=True)