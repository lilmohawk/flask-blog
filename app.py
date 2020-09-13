from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(25), nullable=False, default="N/A")
    content = db.Column(db.Text, nullable = False)

@app.route('/', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        title = request.form["title"]
        author = request.form["author"]
        content = request.form['content']

        NewPost = BlogPost(title = title, author = author, content = content)
        db.session.add(NewPost)
        db.session.commit()

        return redirect("/")
    else:
        post = BlogPost.query.all()
        return render_template("index.html", x = post)

@app.route("/delete/<int:id>")
def delete(id):
    postDel = BlogPost.query.get_or_404(id)
    db.session.delete(postDel)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)