from flask_wtf import FlaskForm
import wtforms as wt


class Check_DB_form(FlaskForm):
    pregnancies = wt.StringField("pregnancies", validators=[
                                 wt.validators.DataRequired()])
    glucose = wt.StringField("glucose", validators=[
                             wt.validators.DataRequired()])
    bloodpressure = wt.StringField("bloodpressure", validators=[
                                   wt.validators.DataRequired()])
    skinthickness = wt.StringField("skinthickness", validators=[
                                   wt.validators.DataRequired()])
    insulin = wt.StringField("insulin", validators=[
                             wt.validators.DataRequired()])
    bmi = wt.StringField("bmi", validators=[wt.validators.DataRequired()])
    diabetespedigreefunction = wt.StringField(
        "diabetespedigreefunction", validators=[wt.validators.DataRequired()])
    age = wt.StringField("age", validators=[wt.validators.DataRequired()])

    submit = wt.SubmitField("submit")
