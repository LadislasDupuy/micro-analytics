from flask import Flask

app = Flask(__name__)

@app.route('/stats')
def stats_page():
    return 'stats'

@app.route('/profile')
def profile_page():
    return 'Mon profil'

@app.route('/produits')
def products_page():
    return 'Nos produits'

@app.route('/')
def home_page():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
