from flask import Flask, jsonify, send_from_directory
import main  # Importe o script com sua lógica de coleta de dados

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_html():
    # Serve o index.html a partir da pasta 'static'
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/data')
def get_data():
    data = main.get_data()  # Supondo que você tem uma função em main.py que retorna os dados
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
