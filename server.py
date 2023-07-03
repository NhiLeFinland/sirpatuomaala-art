from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def home_en():
    return redirect('/')

@app.route('/index-fi.html')
def home_fi():
    return render_template('index-fi.html')

@app.route('/admin')
def admin():
    return 'Admin page'

if __name__ == '__main__':
    app.run()