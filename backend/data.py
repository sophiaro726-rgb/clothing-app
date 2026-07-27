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

@app.route('/searchedreview.php', methods=['GET']) #just get not post bc only searching alr input data 
def searched():
    rbrand = request.args.get('brand')
    rname = request.args.get('name')
    rcategory = request.args.get('category')
    rsize = request.args.get('size')
    rgender = request.args.get('gender')
    rcolor = request.args.get('color')
    ryear = request.args.get('year')
    #rphoto = request.args.get('photo') dont need bc not ssearching by photo 
    selectstring = "SELECT * from clothesinfo WHERE 1=1" #cannot put into execute yet bc we dont know what variables were given in search
    #doing 1=1 bc we ant to run regardless of hwat is input into the search, but we r gonna need to filter the "AND" to what was given
    variablesgiven = []
    if rbrand is not None and rbrand != '': #nneded to add string bc if input nothing string then it wasnt counting as none 
        selectstring = selectstring + " AND LOWER(brand) = %s" #nned to include lowercase bc if input caps different from database 
        variablesgiven.append(rbrand.lower()) #for execute to search for the values needed in list 
    if rname is not None and rname != '':
        selectstring = selectstring + " AND LOWER(name) = %s"
        variablesgiven.append(rname.lower())
    if rcategory is not None and rcategory != '':
        selectstring = selectstring + " AND LOWER(category) = %s"
        variablesgiven.append(rcategory.lower())
    if rsize is not None and rsize != '':
        selectstring = selectstring + " AND LOWER(size) = %s"
        variablesgiven.append(rsize.lower())
    if rgender is not None and rgender != '':
        selectstring = selectstring + " AND LOWER(gender) = %s"
        variablesgiven.append(rgender.lower())
    if rcolor is not None and rcolor != '':
        selectstring = selectstring + " AND LOWER(color) = %s"
        variablesgiven.append(rcolor.lower())
    if ryear is not None and ryear != '':
        selectstring = selectstring + " AND year = %s" #doesnt need lower bc int not text
        variablesgiven.append(ryear)
    curr.execute(selectstring, variablesgiven)
    return curr.fetchall()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000) #starts server w this command & url matches 8000
    #needs to be at end so python grabs everything before 