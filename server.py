from flask import Flask,render_template
from requests import *
from post import Post


post_objects = []
blog_data = get(f"https://api.npoint.io/c790b4d5cab58020d391").json()
for post in blog_data:
    post_objects.append(Post(post["id"],post["title"],post["subtitle"],post["body"]))



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",post_objects=post_objects)

@app.route("/post/<int:num>")
def post(num):
    requested_post = None
    for posts in post_objects:
        if posts.id == num:
            requested_post = posts
    return render_template("post.html",post = requested_post)

@app.route("/contact")
def contact():
    return  render_template("contact.html")

@app.route("/about")
def about():
    return  render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)