from flask import Flask, render_template
import webview
import threading

server = Flask(__name__, static_folder='./static', template_folder='./templates')

@server.route('/')
def home():
    return render_template('index.html')

@server.route('/connect_cell')
def connect_cell():
    return render_template('connect_cell.html')

@server.route('/cellkey')
def cellkey():
    return render_template('cellkey.html')

@server.route('/create_cell')
def create_cell():
    return render_template('create_cell.html')

@server.route('/create_business_cell')
def create_business_cell():
    return render_template('create_business_cell.html')

@server.route('/create_community_cell')
def create_community_cell():
    return render_template('create_community_cell.html')

@server.route('/browser')
def browser():
    return render_template('browser.html')

def run_flask():
    server.run(host='127.0.0.1', port=55000, debug=False)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()


    webview.create_window('Neuronum Browser v1.0.0','http://127.0.0.1:55000',width=1280,height=800,resizable=True)
    webview.start()

