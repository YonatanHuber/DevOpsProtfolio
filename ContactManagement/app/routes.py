from app import chimera_app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@chimera_app.route('/')
@chimera_app.route('/index')
def index():
    return render_template('index.html')

@chimera_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('User {} logged-in successfully, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    else:
        flash('Login failed. Please resubmit correct Username and Password')
    return render_template('login.html', title='Sign In', form=form)

@chimera_app.route('/person')
@chimera_app.route('/person/{id}',methods=['GET'])
def person():
    return render_template('person.html', id = id)
#POST
#PUT
#DELETE
#GET
