from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
    return "hello,dsds"

if __name__=="__main__":
    app.run(debug=True)

import controller.user_controller as user_controller