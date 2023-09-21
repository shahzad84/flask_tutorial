import mysql.connector
import json
from flask import make_response
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
            res=make_response({"payload":result},200)
            res.headers["Access-Control-Allow-Origin"]="*"

            return res
        else:
            return make_response({"message":"No Data Found"},204)
        

    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        return  make_response({"message":"user created sucessfully"},201)
    

    def user_update_model(self,data):
         self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data     ['id']}")
         if self.cur.rowcount>0:
            return  make_response({"message":"updated sucessfully"},201)
         else:
            return  make_response({ "message":"nothing to update"},202)
         

    def user_delete_model(self,id):
         self.cur.execute(f"DELETE FROM users WHERE id={id}")
         if self.cur.rowcount>0:
            return  make_response({"message":"deleted sucessfully"},200)
         else:
            return  make_response({"message":"nothing to delete"},500)

