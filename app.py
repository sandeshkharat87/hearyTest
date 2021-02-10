from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import joblib
from forms import Check_DB_form

model = joblib.load("HEARTDSS.pkl")

app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'


@app.route('/', methods=('GET', 'POST'))
def submit():
    data = None
    # form = MyForm()

    form = Check_DB_form()
    if form.validate_on_submit():
        print(dict(request.form).values)
        data = request.form.to_dict().values()
        data = list(data)[1:-1]
        data = [float(i) for i in data]
        data = model.predict([data])[0]
        print("-------------------------")
        print(data)
        print("-------------------------")

        if data == 0:
            data = "Possitive"
        else:
            data = "Negative"
    else:
        print(form.errors)
    return render_template('home.html', form=form, data=data, )


if __name__ == '__main__':
    app.run(debug=True)
