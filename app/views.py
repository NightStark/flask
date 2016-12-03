from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'lgg'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts = posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    flash(form.validate_on_submit())
    if form.validate_on_submit():
        flash('Login requested for openID="' +
              form.openid.data + '" remember_me=' +
              form.remember_me.data.__str__())
        return redirect('/index')
    else:
        flash("some thing is error.")
    return render_template('login.html', title="Sign In", form=form)


