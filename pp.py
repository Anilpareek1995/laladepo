from flask import Flask,render_template,url_for,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db1'
db = SQLAlchemy(app)


class Lal(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    addd = db.Column(db.String(80))


@app.route("/home", methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':

        name = request.form.get('t2')
        addd = request.form.get('t3')
        entry = Lal(name=name, addd=addd)
        db.session.add(entry)
        db.session.commit()
    return render_template('home.html')


if __name__ == '__main__':
   app.run(debug=True)