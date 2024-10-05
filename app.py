from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Home!'

@app.route('/profile')
def profile():
    return 'This is my profile page'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  
