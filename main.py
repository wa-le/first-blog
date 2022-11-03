from flask import Flask, render_template
from datetime import date
from post import Post
import requests as r

this_year = date.today().year

url = "https://api.npoint.io/fad0c06b9466b8b6720c"
posts = r.get(url).json()
all_post_objects = []
for post in posts:
    each_post_object = Post(post['id'], post['title'], post['subtitle'], post['body'])
    all_post_objects.append(each_post_object)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", current_year=this_year, all_posts=all_post_objects)


@app.route('/posts/<int:index>')
def show_post(index):
    post_requested = None
    for blog_post in all_post_objects:
        if blog_post.id == index:
            post_requested = blog_post
    return render_template("post.html", current_year=this_year, the_post=post_requested)


if __name__ == "__main__":
    app.run(debug=True)
