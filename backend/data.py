from flask import Flask, render_template  #flask is used as the backend to play as the messenger 
#by receiving requests or data and deciding what to do w it
import psycopg2 #for sql
from flask import request 

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
curr = conn.cursor()
#connecting sql and submitted review 
@app.route('/submittedreview.php', methods=['POST']) #just post used not get 
def submitted():
    rbrand = request.form['brand']
    rname = request.form['name']
    rcategory = request.form['category']
    rsize = request.form['size']
    rgender = request.form['gender']
    rcolor = request.form['color']
    ryear = request.form['year']
    if ryear == "":
        ryear =  None #do this bc int type and causes an error
    #photo dif bc file 
    f = request.files['photo'] #diff bc file 
    f.save('static/photos/' + f.filename) #dont want to hardcode name of file so not quotes to save into uploads file for flask 
    rphoto = f.filename
    curr.execute("INSERT INTO clothesinfo (brand, name, category, size, gender, color, year, photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (rbrand, rname, rcategory, rsize, rgender, rcolor, ryear, rphoto))
    # columns, input values and not hard code, and then the variables being input 
    conn.commit()
    return "the test worked"

#conn.close() dont want to shut server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000) #starts server w this command & url matches 8000
    #needs to be at end so python grabs everything before 