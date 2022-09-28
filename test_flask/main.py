from flask import Flask

app = Flask(__name__)

@app.route('/')
def accueil():
    return 'Bienvenue'

@app.route('/home')
def home():
    return "Page home"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)