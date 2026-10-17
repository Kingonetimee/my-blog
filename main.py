from flask import Flask, render_template, request
import requests
import smtplib as sm

MY_EMAIL = "thehalalmatch@gmail.com"
MY_PASSWORD = "vxsp oyah gtpy klpa"

API = "https://api.npoint.io/5fa1df2a610e704c9e4a"

content = requests.get(API)

posts = content.json()

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

@app.route('/contact.html', methods= ['GET', 'POST'])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        email_content = (
            f"Subject: New Blog Contact Form Message\n\n"
            f"Name: {name}\n"
            f"Email Address: {email}\n"
            f"Phone Number: {phone}\n"
            f"Message: {message}"
        )
        with sm.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="ayelekeabdulmuizz@gmail.com",
                msg= email_content.encode('utf-8')
            )
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

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