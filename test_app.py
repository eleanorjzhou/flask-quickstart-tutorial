# Unit test code
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
