from app import app
from flask import request
from model.user_model import user_model
obj=user_model()
@app.route("/user/signup")
def signup():
    return obj.user_signup_model()
@app.route("/user/addone",methods=["POST"])
def addone():
    # print(request.form)
    return obj.user_addone_model(request.form)
@app.route("/user/update",methods=["PUT"])
def update():
    # print(request.form)
    return obj.user_update_model(request.form)