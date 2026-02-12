#!/usr/bin/python3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()

login_id = form.getvalue('loginid')
passwd = form.getvalue('password')

print("Content-type: text/html\n\n")

print("<html><body>")

if login_id is None:
    print("""
        <h2>로그인</h2>
        <form method="post" action="/cgi-bin/login.py">
            아이디: <input type="text" name="loginid"><br><br>
            비밀번호: <input type="password" name="password"><br><br>
            <input type="submit" value="로그인">
        </form>
    """)
else:
    print("<h2>Hello %s</h2>" % login_id)

print("</body></html>")
