import random
import string

from flask import Flask, render_template, request, redirect
from sqlalchemy import or_

from database import db
from models import URL

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()



def generate_code(length=6):
    while True:
        code = ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=length
            )
        )

        existing = URL.query.filter_by(short_code=code).first()

        if not existing:
            return code



@app.route("/")
def home():
    return render_template("index.html")




@app.route("/shorten", methods=["POST"])
def shorten():

    original_url = request.form["url"]

    short_code = generate_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    short_url = request.host_url + short_code

    return render_template(
        "result.html",
        short_url=short_url,
        original_url=original_url
    )




@app.route("/dashboard")
def dashboard():

    search = request.args.get("search")

    if search:
        urls = URL.query.filter(
            or_(
                URL.original_url.contains(search),
                URL.short_code.contains(search)
            )
        ).all()
    else:
        urls = URL.query.order_by(URL.id.desc()).all()

    return render_template(
        "dashboard.html",
        urls=urls,
        search=search
    )




@app.route("/delete/<int:id>")
def delete_url(id):

    url = URL.query.get_or_404(id)

    db.session.delete(url)

    db.session.commit()

    return redirect("/dashboard")




@app.route("/<short_code>")
def redirect_url(short_code):

    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        return redirect(url.original_url)

    return "URL not found!"




if __name__ == "__main__":
    app.run(debug=True)