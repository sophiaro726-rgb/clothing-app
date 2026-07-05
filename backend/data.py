from flask import Flask, render_template  #flask is used as the backend to play as the messenger 
#by receiving requests or data and deciding what to do w it
app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html')
#<link rel="stylesheet" href="{{url_for('static', filename='style.css')}}"> #
#flask has static files for style sheet 
@app.route('/review.html')
def review():
    return render_template('review.html')
@app.route('/search.html')
def search():
    return render_template('search.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000) #starts server w this command
