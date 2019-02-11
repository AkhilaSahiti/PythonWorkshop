import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
cur=conn.cursor()
form=cgi.FieldStorage()
eno=form.getvalue("eno")
ename=form.getvalue("ename")
edept=form.getvalue("edept")
query="update emp SET eno='"+eno"',ename='"+ename"',edept='"+edept"', where eno="eno
try:
    rs=cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("updated Successfully")
finally:
    cur.close()
    conn.close()
