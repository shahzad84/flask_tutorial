import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="password",database="flask",port="1080")
            self.cur=self.con.cursor(dictionary=True)
            print("connected__________!")
        except:
            print("some error")
    def user_signup_model(self):
        self.cur.execute("SELECT* FROM users")
        result=self.cur.fetchall()
        if len(result)>0:
            return json.dumps(result)
        else:
            return "No Data Found"
