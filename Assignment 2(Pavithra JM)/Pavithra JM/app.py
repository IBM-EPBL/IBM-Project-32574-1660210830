from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/blog/<post_id>')
def show_post(post_id):
    return post_id

@app.route("/sign up")
def signup():
    return render_template('sign up.html')
  
@app.route("/sign in")
def signin():
    return render_template('sign in.html')

@app.route("/about")
def about():
     return render_template('about.html')

@app.route("/profiles/<username>")
def profile(username):
    return "hello!" + username






