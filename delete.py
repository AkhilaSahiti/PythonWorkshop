import sqlite3,cgi
print("Content-Type:text/html\r\n\r\n")
conn=sqlite3.connect("gitam.db")
cur=conn.cursor()
form=cgi.FieldStorage()
eno=form.getvalue("eno")
query="delete from emp where eno="+eno
try:
    rs=cur.execute(query)
except Exception as e:
    print(e)
else:
    conn.commit()
    print("Deleted successfully")
finally:
    cur.close()
    conn.close()
    
