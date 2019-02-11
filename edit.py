import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("gitam.db")
cur=conn.cursor()
form=cgi.fieldStorage()
ename=form.getvalue("ename")
query="select * from emp where  ename="+ename
try:
    rs=cur.execute(query)
except Exception as e:
    print(e)
else:
    for record in cur:
        pass
        html='''<html>
        <body>
        <form action="update.py"method="put">
        eno:<input type="text" value="%s"name="eno">
        ename:<input type="text" value="%s" name="ename">
        edept:<input type="text" value="%s" name="edept">
        <input type="submit" value="update">
        </from>
        </body>
        </html>'''%(str(record[1], record[2]))
        print(html)
finally:
    cur close()
    conn close()
