from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def hash_message():
    message = request.form['message']
    md5_hash = hashlib.md5(message.encode()).hexdigest()
    return md5_hash

if __name__ == '__main__':
    app.run(debug=True)
x