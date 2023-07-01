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
