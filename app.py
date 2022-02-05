# [Background Tasks in Python with RQ] https://devcenter.heroku.com/articles/python-rq
# [Worker Dynos, Background Jobs and Queueing] https://devcenter.heroku.com/articles/background-jobs-queueing
# [Google Sheets API v4 - Python Quickstart] https://developers.google.com/sheets/api/quickstart/python
# [Google Shhets API v4 - Updating Spreadsheets] https://developers.google.com/sheets/api/guides/batchupdate
# [Reading & Writing Cell Values] https://developers.google.com/sheets/api/guides/values
# [Method: spreadsheets.values.append] https://developers.google.com/sheets/api/guides/values#appending_values
# https://developers.google.com/sheets/api/samples/writing#append_values


import requests
from flask import Flask, render_template
import os
import sys
import threading
import time


app = Flask(__name__)


@app.route("/")
def index():
    # Load current RSS
    wp_login = 'http://www.izaax.net/blog/wp-login.php'
    rss_feed = 'http://www.izaax.net/blog/?feed=rss2'
    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')

    with requests.Session() as s:
        headers1 = { 'Cookie':'wordpress_test_cookie=WP Cookie check' }
        datas={ 
            'log':username, 'pwd':password, 'wp-submit':'Log In', 
            'redirect_to':rss_feed, 'testcookie':'1'  
        }
        s.post(wp_login, headers=headers1, data=datas)
        resp = s.get(rss_feed)
        content = resp.text

    # Render HTML with count variable
    return render_template("index.html", feed=content)


# Run the app	
	
if __name__ == '__main__':
	app.run()