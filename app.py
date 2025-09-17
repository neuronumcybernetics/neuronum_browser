from flask import Flask, render_template
import webview
import threading

server = Flask(__name__, static_folder='./static', template_folder='./templates')

@server.route('/')
def home():
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

@server.route('/nodes')
def nodes():
    return render_template('nodes.html')

@server.route('/neuronum_cellai')
def neuronum_cellai():
    return render_template('neuronum_cellai.html')

def run_flask():
    server.run(host='127.0.0.1', port=55000, debug=False)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()


    webview.create_window('Neuronum CELLai v1.0.2','http://127.0.0.1:55000',width=1280,height=800,resizable=True)
    webview.start()

