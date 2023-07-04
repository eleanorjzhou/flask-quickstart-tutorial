# Flask Quickstart Tutorial

Here is the [project layout](https://flask.palletsprojects.com/en/latest/tutorial/layout/) to follow.

## Day 1 - Steps to Install and Run a Simple Flask App (Windows)

We can create the `app.py` file in the project folder beforehand.

1. Create an virtual environment in the project folder with command `py -3 -m venv .venv`
2. In the project folder, activate the virtual env. by running `.venv\Scripts\activate`
3. While the virtual env. is activated, install Flask with `pip install Flask`
4. To exit virtual env. we need to deactivate it with `deactivate`
5. To serve the app, virtual env. needs to be activated before running `flask run` (or `flask --app app-name run` if the app is not named `app.py`)


## Day 2 - Routing

### Best practices for routing in Flask
- Use meaningful and descriptive route URLs to improve readability and maintainability.
- Consider RESTful principles when designing your routes for APIs.
- Organize routes logically based on the application's structure and functionality.

### Links
In order for the links to render, we need to make sure that the following are in place:
- In the template, the link should look like this: `<a href="{{ url_for('def_routeName') }}">RouteName</a>`
- In `App.py`, we should have `@app.route('/routeName')` and `def def_routeName()`
- Note that when routing `index.html`, `App.py` should have `@app.route('/')` instead

### Unique URLs / Redirection Behavior
Adding a trailing slash `/` to the endpoint will allow Flask to redirect user to the canonical URL when accessing the URL without a trailing slash. This will prevent the `404 Not Found` error. Not using the trailing slash helps keep URLs unique for resources and helps search engines avoid indexing the same page twice.

### URL Building
URL building in Flask is the process of generating URLs dynamically based on the defined routes and any variables associated with them. 
To build a URL to a specific function, use the `url_for()` function.

### HTTP Methods
HTTP methods are like instructions that tell the server what action to perform when interacting with a web application. The most common methods are `GET` and `POST`. `GET` is used to retrieve data, like viewing a webpage, while `POST` is used to send data, like submitting a form or creating a new resource on the server.

### Variable Rules
Variable rules in Flask allow you to capture dynamic parts of a URL, like usernames or product IDs. They act like placeholders in your routes. For example, if you have a route `'/user/<username>'`, the `'<username>'` part can be any value, and Flask will pass it as a parameter to the corresponding view function, enabling dynamic content generation based on the URL input.


## Day 3 - Static Files and Rendering Templates

To style this app, we will create a custom CSS stylesheet (directory: `static/css/style.css`) which will import the [Bulma](https://bulma.io/documentation/) CSS Framework.

### Static Files
Getting the css file to work we use `url_for('static', filename='css/style.css')`.

### Rendering Templates
To render a template we need to use the `render_template()` function
- In `app.py`, import the function with `from flask import render_template`
- Then we need to return the template: 
```
@app.route('/route/')
def template(name=None):
    return render_template('template.html', name=name)
```


## Day 4 - Accessing Request Data

### Context Locals
We can use context locals to implement unit testing:
- `test_request_context()` allows you to create a simulated request context to test parts of our Flask app
- The code that utilizes `test_request_context()` should typically be added in a separate testing file or within a testing framework such as `pytest`
- Example:
```
# test_app.py Unit test code

from flask import request
from app import app, greet

def test_greet_route_with_name():
    with app.test_request_context('/greet?name=Jack', method='GET'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/greet' # checks if the path of the request matches '/greet', ensuring that the expected route is being accessed
        assert request.method == 'GET' # verifies that the HTTP method of the request is set to 'GET', ensuring that the expected method is being used
        assert request.args.get('name') == 'Jack' # checks if the value of the 'name' query parameter in the test request context is 'John'. It ensures that the parameter is correctly passed and accessible in the request.args dictionary
        response = greet() # calls the greet() function within the test request context. It captures the response returned by the function
        assert response == "Hello, Jack!" # checks if the response returned by the greet() function is equal to the expected value "Hello, John!". It verifies that the greet() function behaves as expected based on the provided request context
```

### The Request Object
The `request` object in Flask provides access to various attributes and methods that allow you to work with the data sent in an HTTP request.
- Example: Access form data
```
# This is an example of a simple login by validating form data fetched by the GET method

# In app.py

from flask import request  # HTTP Methods
from login_utils import validate_login # Login validation

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


# In login_utils.py

def validate_login(username, password):
    # Perform validation logic here
    if username == 'PineappleJack' and password == '12345':
        return True
    else:
        return False

```


### File Uploads
1. In HTML form, set the attribute `enctype="multipart/form-data"`, for example:
```
<form action="/upload" method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
```
2. In `app.py`:
```
from werkzeug.utils import secure_filename # Optional - Use if you want to use the filename of the client to store the file on the server


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():

    message = None

    if request.method == 'POST':

        file = request.files['file'] # access the uploaded file

        if file:

            # Process the uploaded file
            filename = file.filename
            file.save(f"var/www/uploads/{filename}") # save the file

            # To use the filename of the client to store the file on the server
            # file.save(f"var/www/uploads/{secure_filename(filename)}")
        
        else:

            message = "No file selected."
            
    return render_template('upload.html', message=message)
```


### Cookies
Cookies are small pieces of data stored on the client-side (user's browser) by a website. They are used to store information that can be accessed and retrieved by the website or server on subsequent visits or requests.
- Note: If you want to use sessions, do not use the cookies directly but instead use the Sessions in Flask that add some security on top of cookies for you.
- Reading cookies:
```
from flask import request

@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a KeyError if the cookie is missing.
```
- Setting/Storing cookies:
```
from flask import make_response

@app.route('/')
def index():
    res = make_response(render_template(...))
    res.set_cookie('username', 'PineappleJack', max_age=3600, secure=True, httponly=True)
    return res
```
- max_age: The maximum age of the cookie in seconds (in this case, it expires after 3600 seconds or 1 hour).
- secure: The cookie will only be sent over a secure (HTTPS) connection.
- httponly: The cookie cannot be accessed or modified by client-side JavaScript, enhancing security against certain types of attacks.

