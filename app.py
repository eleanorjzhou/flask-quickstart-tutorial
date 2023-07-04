from flask import Flask
from flask import render_template  # To render a template
from flask import url_for  # To build a URL to a specific function
from flask import request  # HTTP Methods
from login_utils import validate_login # Login validation
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home(name=None): # 
    return render_template('index.html', name=name)

@app.route('/desserts/')
def desserts():
    return "Here are some delicious dessert recipes!"

@app.route('/appetizers/')
def appetizers():
    return "Check out these tasty appetizer recipes!"

@app.route('/main-courses/')
def main_courses():
    return "Discover a variety of flavorful main course recipes!"


# URL Building
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('profile', username='Pineapple Jack')) # This will print out in the console "/user/Pineapple%20Jack"


# HTTP Methods - All methods in one function
@app.route('/login/', methods=['GET', 'POST'])
def login(name=None):

    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Perform login authentication and validation
        if validate_login(username, password):

            # Redirect to a different page or return a response based on the authentication result
            return f'Welcome, {username}! Login successful.'
    
        else:

            error = 'Invalid username/password'

    return render_template('login.html', error=error) # Show the login form
    

# HTTP Methods Alternative - Separate views for different methods into different functions
"""
@app.get('/login/')
def login_get():
    return show_the_login_form()

@app.post('/login/')
def login_post():
    return do_the_login()
"""

# Context Locals - Example
@app.route('/greet/', methods=['GET'])
def greet():

    username = request.args.get('name')

    if username:
        return f"Hello, {username}!"
    else:
        return "Hello, anonymous user!"
    

# File Uploads
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    message = None

    if request.method == 'POST':

        file = request.files['file'] # access the uploaded file

        if file:

            # Process the uploaded file
            filename = file.filename
            file.save(f"var/www/uploads/{filename}") # save the file

            # To use the filename of the client to store the file on the server, pass it through the secure_filename() function
            # file.save(f"var/www/uploads/{secure_filename(filename)}")
        
        else:

            message = "No file selected."
            
    return render_template('upload.html', message=message)
