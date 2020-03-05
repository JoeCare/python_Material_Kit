import eel
import sqlite3
#create the db if not exist
dbconnection = sqlite3.connect('db/project.db')

#opening the connection





eel.init('web')

@eel.expose
def createUser(record):
    cursor = dbconnection.cursor()
    data = []
    data = record
    sql = """CREATE TABLE IF NOT EXISTS USERS_TABLE 
                (UID INTEGER PRIMARY KEY AUTOINCREMENT,
                USERNAME VARCHAR(100),
                EMAIL_ID VARCHAR(100),
                PASSWORD VARCHAR(100),
                CPASSWORD VARCHAR(100))"""
    cursor.execute(sql)
    sql = "INSERT INTO USERS_TABLE (USERNAME,EMAIL_ID,PASSWORD,CPASSWORD) VALUES(?,?,?,?),(data['username'],data['useremail'],data['password'],data['confirm_password'])"
    #sql = "INSERT INTO USERS_TABLE (USERNAME,EMAIL_ID,PASSWORD,CPASSWORD) VALUES('Ram','Ram@gmail.com','SAMPLE','SAMPLE')"
    cursor.execute(sql)
    sql = "select * from USERS_TABLE"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    dbconnection.close()
    eel.success_message()





eel.start('template.html',size=(1240,820))