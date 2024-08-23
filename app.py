from flask import Flask, jsonify, send_from_directory
import main

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_html():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/data')
def get_data():
    data = main.get_data()  
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
