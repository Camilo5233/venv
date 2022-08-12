from werkzeug.security import check_password_hash
from forms import FormLogin, FormSignin

class User():
    

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

