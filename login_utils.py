# login_utils.py 
# Login validation

def validate_login(username, password):
    # Perform validation logic here
    if username == 'PineappleJack' and password == '12345':
        print("Correct cred")
        return True
    else:
        print("Incorrect cred")
        return False
