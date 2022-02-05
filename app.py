import os
import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/feed")
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
    return render_template("index.html", content=content)


# Run the app	
	
if __name__ == '__main__':
	app.run()