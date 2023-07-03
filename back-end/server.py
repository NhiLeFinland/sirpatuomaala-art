from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/admin')
def admin():
    return 'Admin page'

if __name__ == '__main__':
    app.run()