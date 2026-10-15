from flask import Flask, render_template
import requests

API = "https://api.npoint.io/5fa1df2a610e704c9e4a"

content = requests.get(API)

posts = content.json()
print(posts)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts = posts)

@app.route('/index.html')
def index():
    return render_template("index.html", all_posts = posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/post.html/<int:index>')
def show_post(index):
    requested_post = None
    for blog in posts:
        if blog["id"] == index:
            requested_post = blog
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)