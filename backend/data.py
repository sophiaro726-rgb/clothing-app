from flask import Flask #flask is used as the backend to play as the messenger 
#by receiving requests or data and deciding what to do w it
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Server is running'

if __name__ == '__main__':
    app.run()
