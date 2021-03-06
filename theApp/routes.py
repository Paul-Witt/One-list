from flask import render_template # render pages
from theApp import app
from theApp.forms import LoginForm
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index():
    # For debuging
    if app.debug:
        pass

    user = "Paul"
    return render_template('index.html', title='Home', user=user, stuff=app.config)
    

@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
               form.username.data, form.remember_me.data))

        #return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)