from flask import Flask, render_template  #flask is used as the backend to play as the messenger 
#by receiving requests or data and deciding what to do w it
import psycopg2

app = Flask(__name__)

@app.route('/')
def intro():
    return render_template('intro.html') #grabs templates I made (as html) and applies to web page 
#<link rel="stylesheet" href="{{url_for('static', filename='style.css')}}"> #
#flask has static files for style sheet 
@app.route('/review.html')
def review():
    return render_template('review.html')
@app.route('/search.html')
def search():
    return render_template('search.html')

#POSTGRES CODE
hostname = 'localhost'
database = 'clothing_app' #what i named the db
username = 'postgres'
port_id = 5432

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
    port = port_id
)
cur = conn.cursor()
#conn.close() dont want to shut server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000) #starts server w this command & url matches 8000
    #needs to br at end so python grabs everything before 