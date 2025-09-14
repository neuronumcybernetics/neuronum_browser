from flask import Flask, render_template
import webview
import threading

# Create Flask app
server = Flask(__name__, static_folder='./static', template_folder='./templates')

@server.route('/')
def home():
    # Render your home.html (make sure it exists inside templates folder)
    return render_template('home.html')

@server.route('/connect_cell')
def connect_cell():
    return render_template('connect_cell.html')

@server.route('/cellkey')
def cellkey():
    return render_template('cellkey.html')

@server.route('/create_cell')
def create_cell():
    return render_template('create_cell.html')

@server.route('/neuronum_cellai')
def neuronum_cellai():
    return render_template('neuronum_cellai.html')

def run_flask():
    # Run flask app (with no debug and on localhost)
    server.run(host='127.0.0.1', port=5000, debug=False)

if __name__ == '__main__':
    # Run flask in a separate thread so webview can start after server is ready
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()


    webview.create_window(
    'Neuronum CELLai v1.0.2',
    'http://127.0.0.1:5000',
    width=1280,
    height=800,
    resizable=True  # Optional: allow resizing
    )
    webview.start()

