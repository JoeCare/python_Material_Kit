import eel
import sqlite3
#create the db if not exist
dbconn = sqlite3.connect('db/project.db')

#opening the connection

conn = dbconn.cursor()

eel.init('web')

eel.start('template.html',size=(1240,820))