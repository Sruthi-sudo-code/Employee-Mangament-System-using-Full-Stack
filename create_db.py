
import sqlite3 as sql
con = sql.connect('db_web.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS users")
sql ='''CREATE TABLE "users" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"UNAME"	TEXT,
	"CONTACT"	INTEGER,
    "EMAIL" TEXT,
    "ADDRESS" TEXT,
    "DESIGINATION" TEXT,
    "SALARY" INTEGER
)'''
cur.execute(sql)
con.commit()
con.close()
