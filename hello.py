#!/usr/bin/env python3
import os
import json
import templates
import cgi
import secret


def main():

    # Question 1
    '''
    for k in os.environ.keys():
        print(f"{k}: {os.environ[k]}")
    '''

    '''
    environment_json = json.dumps(dict(os.environ), indent=4)
    print("<h3>JSON Environment</h3>")
    print(f"<p>{environment_json}</p>")
    '''

    # Question 2
    '''
    queries = os.environ["QUERY_STRING"].split('&')
    print("<h3>Query Parameters</h3>")
    for q in queries:
        print(f"<p>{q}</p>")
    '''
    # Question 3
    '''
    print("<h3>Browser</h3>")
    print(f"<p>{os.environ['HTTP_USER_AGENT']}</p>")
    '''
    # Question 4, 5, 6
    form = cgi.FieldStorage()
    username = form.getvalue("username")
    password = form.getvalue("password")

    cookies = [c.strip() for c in os.environ.get("HTTP_COOKIE").split(';')]
    login_cookie = "LoggedIn=true" in cookies
    if login_cookie:
        print(templates.secret_page(secret.username, secret.password))

    elif not (username and password):
        print(templates.login_page())
    else:
        login_immediate = False
        if username == secret.username and password == secret.password:
            print("Set-Cookie:LoggedIn=true;", end="")
            login_immediate = True

        if login_immediate:
            print(templates.secret_page(username, password))
        else:
            print(templates.after_login_incorrect())


if __name__ == '__main__':
    main()
