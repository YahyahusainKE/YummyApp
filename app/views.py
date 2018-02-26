from flask import Flask, render_template, flash, redirect, sessions, url_for, logging, request
from wtforms import Form, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import userdata, User
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'Provide platform to store and also share recipes'


class SignupForm(Form):
    First_name = StringField('First-Name', [validators.Length(min=4, max=50)])
    Last_name = StringField('Last-Name', [validators.Length(min=4, max=50)])
    Email = StringField('Email', [validators.Length(min=6, max=30)])
    Password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Password do not match')
    ])
    Confirm = PasswordField('Confirm Password')


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignupForm(request.form)
    if request.method == 'POST'and form.validate():
        firstname = form.First_name.data
        lastname = form.Last_name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.Password.data))
        confirm = form.Confirm.data
        User(firstname, lastname, email, password, confirm)
    return render_template('sign-up.html', form=form)

    
if __name__ == '__main__':
    app.run(debug=True)