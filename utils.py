from werkzeug.security import generate_password_hash, check_password_hash    

def set_password(password: str):
        return  generate_password_hash(password)

def check_password(password: str, hash: str):
    return check_password_hash(hash, password)