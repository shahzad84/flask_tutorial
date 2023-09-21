import mysql.connector
import json
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="password",database="flask",port="1080")
            self.con.autocommit=True
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
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return "user created sucessfully"
    def user_update_model(self,data):
         self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data     ['id']}")
         if self.cur.rowcount>0:
            return "updated sucessfully"
         else:
            return "nothing to update"
    def user_delete_model(self,id):
         self.cur.execute(f"DELETE FROM users WHERE id={id}")
         if self.cur.rowcount>0:
            return "deleted sucessfully"
         else:
            return "nothing to delete"

