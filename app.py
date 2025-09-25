from flask import Flask, render_template, request, jsonify
import webview
import threading
from pathlib import Path
from dotenv import load_dotenv
import os

server = Flask(__name__, static_folder='./static', template_folder='./templates')

@server.route('/')
def home():  
    return render_template('index.html')

@server.route('/connect_cell')
def connect_cell():
    credentials_folder_path = Path.home() / ".neuronum"
    env_path = credentials_folder_path / ".env"

    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        
        if email and password:
            print(email, password)
            return render_template('connect_cell.html', email=email, password=password)
            
    return render_template('connect_cell.html')

@server.route('/cellkey')
def cellkey():
    return render_template('cellkey.html')

@server.route('/create_cell')
def create_cell():
    return render_template('create_cell.html')

@server.route('/create_community_cell')
def create_community_cell():
    return render_template('create_community_cell.html')

@server.route('/browser')
def browser():
    return render_template('browser.html')


@server.route('/store_credentials', methods=['POST'])
def store_credentials():
    data = request.get_json()
    if data:
        email = data.get('email')
        host = data.get('host')
        password = data.get('password')
        synapse = data.get('synapse')
        
        if not email or not host:
            return jsonify({'status': 'error', 'message': 'Missing email or host data'}), 400

        try:
            credentials_folder_path = Path.home() / ".neuronum"
            credentials_folder_path.mkdir(parents=True, exist_ok=True)
            
            env_path = credentials_folder_path / ".env"
            env_path.write_text(f"HOST={host}\nPASSWORD={password}\nNETWORK=neuronum.net\nSYNAPSE={synapse}\nEMAIL={email}")
            
            print(f"Credentials saved: Email: {email}, Host: {host}")
            
            return jsonify({'status': 'success', 'message': 'Credentials saved successfully'})
        
        except Exception as e:
            print(f"Error saving credentials: {e}")
            return jsonify({'status': 'error', 'message': 'Failed to save credentials'}), 500
    
    return jsonify({'status': 'error', 'message': 'Invalid data'}), 400
        

def run_flask():
    server.run(host='127.0.0.1', port=55000, debug=False)

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    webview.create_window('Neuronum Network v1.0.0','http://127.0.0.1:55000',width=1280,height=800,resizable=True)
    webview.start()

