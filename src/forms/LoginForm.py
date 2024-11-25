from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, HiddenField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp, ValidationError

VERBOTENE_WOERTER = ['beleidigung']


def verbotene_woerter_check(form, field):
    input_value = field.data.lower()
    for wort in VERBOTENE_WOERTER:

        if wort.lower() in input_value:
            raise ValidationError(
                f"Das Wort '{wort}' ist verboten. Bitte verwenden Sie keine beleidigenden Ausdrücke.")


class LoginForm(FlaskForm):
    login = StringField(
        'Login',
        validators=[
            verbotene_woerter_check,
            DataRequired(),
            Length(
                3,
                40,
                message="Der Name muss zwischen 3 und 40 Zeichen lang sein.")],
        render_kw={
            "placeholder": "Login"},
        name="username")
    password = PasswordField(
        'Password',
        validators=[
            verbotene_woerter_check,
            DataRequired(),
            Length(
                3,
                40,
                message="Password muss zwischen 3 und 40 Zeichen lang sein.")],
        render_kw={
            "placeholder": "*********"},
        name="password")

