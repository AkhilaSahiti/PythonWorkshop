import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("gitam.db")
cur=conn.cursor()
form=cgi.FieldStorage()
eno=form.getvalue("eno")
ename=form.getvalue("ename")
edept=form.getvalue("edept")
query="insert into emp values('"+eno+"','"+ename+"','"+edept+"')"
try:
    rs=cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("successfully inserted")
cur.close()
conn.close()
