from flask import Flask, render_template  #flask is used as the backend to play as the messenger 
#by receiving requests or data and deciding what to do w it
import psycopg2 #for sql
from flask import request, session #session for cookies and login save 
import bcrypt
#.env to secure password when make public link (doesn't get pushed publically)
from dotenv import load_dotenv #from https://pypi.org/project/python-dotenv/
import os 

load_dotenv()  # reads variables from a .env file and sets them in os.environ

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
@app.route('/signup.html')
def makeaccount():
    return render_template('signup.html')
@app.route('/login.html')
def existingaccount():
    return render_template('login.html')


#POSTGRES CODE
hostname = os.getenv('hostname')
database = os.getenv('database')
publicusername = os.getenv('publicusername') #cant j be username bc reading my Windows username
port_id = os.getenv('port_id')
secretpassword = os.getenv('secretpassword')
app.secret_key = os.getenv('app.secret_key')

conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = publicusername,
    port = port_id,
    password = secretpassword #needs to have this name, ok if repeated bc j inside route 
)
curr = conn.cursor()
#connecting sql and submitted review 
@app.route('/submittedreview.php', methods=['POST']) #just post used not get 
def submitted():
    if 'userid' not in session:
        return 'ERROR: Please sign into an account to continue'
    rbrand = request.form['brand']
    rname = request.form['name']
    rcategory = request.form['category']
    rsize = request.form['size']
    rheight = request.form['height']
    rweight = request.form['weight']
    rgender = request.form['gender']
    rcolor = request.form['color']
    ryear = request.form['year']
    if ryear == "":
        ryear =  None #do this bc int type and causes an error
    #photo dif bc file
    if rgender == "":
        rgender =  None 
    if rheight == "":
        rheight =  None
    if rweight == "":
        rweight =  None
    if rcolor == "":
        rcolor =  None
    f = request.files['photo'] #diff bc file 
    f.save('static/photos/' + f.filename) #dont want to hardcode name of file so not quotes to save into uploads file for flask 
    rphoto = f.filename
    ruserid = session['userid']
    rcomment = request.form['comment']
    if rcategory == "Shirts" and (rheight == '' or rweight == ''):
        return "ERROR: Height and weight are required for shirt uploads"
    curr.execute("INSERT INTO clothesinfo (brand, name, category, size, gender, color, year, photo, userid, comment, height, weight) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (rbrand, rname, rcategory, rsize, rgender, rcolor, ryear, rphoto, ruserid, rcomment, rheight, rweight))
    # columns, input values and not hard code, and then the variables being input 
    conn.commit()
    return "Your review was submitted"

@app.route('/searchedreview.php', methods=['GET']) #just get not post bc only searching alr input data 
def searched():
    rbrand = request.args.get('brand')
    rname = request.args.get('name')
    rcategory = request.args.get('category')
    rsize = request.args.get('size')
    rgender = request.args.get('gender')
    rcolor = request.args.get('color')
    ryear = request.args.get('year')
    rheight = request.args.get('height')
    rweight = request.args.get('weight')
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
    if rheight is not None and rheight != '':
        selectstring = selectstring + " AND LOWER(height) = %s"
        variablesgiven.append(rheight.lower())
    if rweight is not None and rweight != '':
            selectstring = selectstring + " AND LOWER(weight) = %s"
            variablesgiven.append(rweight.lower())
    curr.execute(selectstring, variablesgiven)
    res = curr.fetchall() #before dict it prints as j a list of each value w out key attached to value 
    dictlist = [] #since gonna have multiple outpets, needs to be a list of dictionaries connecting the variables to the values
    for vlist in res:
        vdict = {
            'id' : vlist[0], #starts w index
            'brand' : vlist[1],
            'name' : vlist[2],
            'category' : vlist[3],
            'size' : vlist[4],
            'gender' : vlist[5],
            'color' : vlist[6],
            'year' : vlist[7],
            'photo' : vlist[8], #need photo now bc this is the returned result 
            'comment' : vlist[10], #need comment bc returned result not searched & 9 is userid added
            'height' : vlist[11],
            'weight': vlist[12]
        }
        dictlist.append(vdict)
    return render_template('search.html', results = dictlist) #need results name bc unlike other pages it needs to grab info for as much data that matches the searched results

def hash_pwd(password:str, rounds=12) -> bytes: #https://www.youtube.com/watch?v=YIUNTJEQwQ4
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
    return pwd 

@app.route('/signup.php', methods=['POST']) #just post used not get 
def signup():
    remail = request.form['email']
    rpassword = request.form['password']
    hpassword = hash_pwd(rpassword).decode() #in bytes so decode it to string bc TEXT type
    curr.execute("INSERT INTO userinfo (email, hashpassword) VALUES (%s, %s)", (remail, hpassword))
    conn.commit()
    return "The account was created"

@app.route('/login.php', methods=['POST']) #just post used not get 
def login():
    remail = request.form['email']
    rpassword = request.form['password']
    curr.execute("SELECT id, email, hashpassword FROM userinfo WHERE email = %s", (remail,))
    res = curr.fetchone() #emails r unique so fetchone bc only 1 to grab if all different
    if res is None:
        return "ERROR: An existing account does not exist with this email"
    else:
        check = bcrypt.checkpw(rpassword.encode(), res[2].encode()) #need to encode pass bc need convert back to bytes 
        if check is True:
            session['userid'] = res[0] #id wasnt given ny user bc used email to sign in so need to grab id from table and set to session 
            return f'Logged in as {session["userid"]}' #taken directly from flask website
            #return "Login successful. Welcome back!"
        else:
            return "ERROR: Incorrect password"
        
@app.route('/logout')
def logout():
    # remove the username from the session if it's there (FROM FLASK PAGE)
    session.pop('userid', None)
    return "You have been logged out"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8000) #starts server w this command & url matches 8000
    #needs to be at end so python grabs everything before 