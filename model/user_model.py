import mysql.connector
class user_model():
    def __init__(self):
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="password",database="flask",port="1080")
            print("connected__________!")
        except:
            print("some error")
    def user_signup_model(self):
        return "hii this is model"
