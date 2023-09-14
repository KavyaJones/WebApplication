from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.SignInForm import SigninForm
from forms.SignUpForm import SignupForm
from forms.DataForm import DataForm
from orm.orm import sqlalchemy_instance as db
from orm.user import User, UserData

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = 'your_secret_key'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'signin'
login_manager.init_app(app)

User.user_data = db.relationship('UserData', back_populates='user', lazy='dynamic')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please sign in.', 'success')
            return redirect(url_for('signin'))
    return render_template('auth/signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('PostLoginLanding'))
        flash('Invalid credentials. Please try again.', 'danger')
    return render_template('auth/signin.html', form=form)

@app.route('/')
def PreLoginLanding():
    return render_template('base.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('PreLoginLanding'))


@app.route('/postlogin', methods=['GET', 'POST'])
@login_required
def PostLoginLanding():
    form = DataForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data


        user_data = UserData(name=name, email=email, user=current_user)

        db.session.add(user_data)
        db.session.commit()

        flash('Data submitted successfully!', 'success')


    user_data = current_user.user_data.all()

    return render_template('application.html', form=form, user_data=user_data)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
