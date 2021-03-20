from flask import Flask,render_template,request
# Data BAse
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///no3.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class rajput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'My Name is {self.username}{self.id}{self.email}'


@app.route('/')
def hello_world():
    # admin = rajput(username='admin', email='admin@example.com')
    # guest = rajput(username='guest', email='guest@example.com')
    raj = rajput.query.all();
    print(raj)
    # admin = rajput()
    # guest= rajput()
    # db.session.add(admin)
    # db.session.add(guest)
    # db.session.commit()
    return render_template('student.html')
@app.route('/result', methods=['GET', 'POST'])
def Result():
    if request.method == 'POST':
        result = request.form
        result1 = result['chemistry']
    print(result)
    print(result1)
    print(dict(result))
    result=dict(result)


    admin = rajput(username=result['Name'],email=result['Physics']+'p@gmail.com')
    guest= rajput(username=result['Name']+'bhai',email=result['chemistry']+'@gmail.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
