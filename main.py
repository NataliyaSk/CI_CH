
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)
@app.route('/mult', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a и b - не тот формат'
    return str(a * b)

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()