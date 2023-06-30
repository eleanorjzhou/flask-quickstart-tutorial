from flask import Flask
from flask import render_template  # To render a template
from flask import url_for  # To build a URL to a specific function
from flask import request  # HTTP Methods

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
@app.route('/login', methods=['GET', 'POST'])
def login(name=None):
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Perform login authentication and validation
        # Redirect to a different page or return a response based on the authentication result
        return f'Welcome, {username}! Login successful.'
    else:
        return render_template('login.html', name=name) # Show the login form
    

# HTTP Methods Alternative - Separate views for different methods into different functions
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()