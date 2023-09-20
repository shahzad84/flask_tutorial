from app import app
from model.user_model import user_model
obj=user_model()
@app.route("/user/signup")
def signup():
    return obj.user_signup_model()