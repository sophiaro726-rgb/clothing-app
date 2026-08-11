from data import hash_pwd #checking hash_pwd function from data.py
from data import app as approute #need to rename bc def is app from flask docs example and is going to override 
import pytest #for fixture 


# content of test_sample.py
#def func(x):
 #   return x + 1
#def test_answer():
 #   assert func(3) == 5
 
def test_checkhashpwd(): #need a test_ bc need pytest to read it and not skip over 
    testpassword = 'abc123'
    check1 = hash_pwd(testpassword)
    check2 = hash_pwd(testpassword)
    assert check1 != check2 #dont want them to be the same hash even though same password

#def test_request_example(client): https://flask.palletsprojects.com/en/stable/testing/
 #def test_edit_user(client):
    #esponse = client.post("/user/2/edit", data={
      #  "name": "Flask",
       # "theme": "dark",
       # "picture": (resources / "picture.png").open("rb"),
    #})
    #assert response.status_code == 200
def test_loginfail_example(client):
    response = client.post("/login.php", data = {
        "email" : "test@aol.com",
        "password" : "notright101" #not password paired with example tester email
        }
    )
    assert b"ERROR: Incorrect password" in response.data #testing that if the wrong password is input that this will be the return for the user 

def test_loginsuccess_example(client):
    response = client.post("/login.php", data = {
        "email" : "test@aol.com",
        "password" : "test123" #not password paired with example tester email
        }
    )
    assert b"Logged in as" in response.data #since not grabbing userid from sql, it is checking if it wirtes these words to show it is somehwere in response and technically isnt 100% showing if correct bc not testing userid but j return statement consisting of text 

@pytest.fixture() #use one to not have to repeat testing app w diff tests
def app():
    #app = create_app() DONT NEED i alr reated @app routes in my data 
    approute.config.update({
        "TESTING": True,
    })

    yield approute



@pytest.fixture()
def client(app):
    return app.test_client()