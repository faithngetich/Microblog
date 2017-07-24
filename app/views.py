from app import app
from flask import render_template
from .forms import LoginForm

# index function supressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm
    return render_template('login.html',
                            title='SIgn In',
                            form=form)