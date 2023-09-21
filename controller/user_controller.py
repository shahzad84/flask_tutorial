
from datetime import datetime
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
    return obj.user_update_model(request.form)
@app.route("/user/delete/<id>",methods=["DELETE"])
def delete(id):
    return obj.user_delete_model(id)
@app.route("/user/patch/<id>",methods=["PATCH"])
def patch(id):
    return obj.user_patch_model(request.form,id)
@app.route("/user/signup/limit/<limit>/page/<page>",methods=["GET"])
def pagination(limit,page):
    return obj.user_pagination_model(limit,page)


@app.route("/user/<uid>/upload/avatar", methods=["PUT"])
def upload_avatar(uid):
    file = request.files['avatar']
    new_filename =  str(datetime.now().timestamp()).replace(".", "") # Generating unique name for the file
    split_filename = file.filename.split(".") # Spliting ORIGINAL filename to seperate extenstion
    ext_pos = len(split_filename)-1 # Canlculating last index of the list got by splitting the filname
    ext = split_filename[ext_pos] # Using last index to get the file extension
    db_path = f"uploads/{new_filename}.{ext}"
    file.save(f"uploads/{new_filename}.{ext}")
    return obj.upload_avatar_model(uid, db_path)