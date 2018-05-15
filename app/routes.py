from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'JD'}
    posts = [
        {
            'author' : { 'username':'AB' },
            'body' : 'What is life but a reason to live fully?'
        },
        {
            'author' : { 'username':'VK' },
            'body' : 'History has shown that huslers will hustle'
        }
    ]
    return render_template('index.html',title='home',user=user, posts=posts)
