from flask import Blueprint, render_template, request, redirect, url_for, flash
from ceevee_backend.models.user import User
from flask_login import current_user, login_user, logout_user, login_required
from ceevee_backend import bcrypt
from ceevee_backend.users.forms import LoginForm, RegisterForm
users = Blueprint("users", __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    """ Users register route"""
    if current_user.is_authenticated:
        return redirect(url_for("users.home")

    form = RegisterForm()
    if form.validate_on_submit():
       hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
       user= User(first_name=form.first_name.data, last_name=form.last_name.data, 
             email=form.email.data, password=hashed_password)
       user.roles.append(form.roles.data)
       db.session.add(user)
       db.session.commit()
       flash(f'Account created for {form.email.data}! you''re now able to login', 'success')
       return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    """ The Users applications login route"""
    if current_user.is_authenticated:
        return redirect(url_for("users.home")

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.rememberMe.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.home'))
        else:
            flash("Login unsuccessful, please check email or password!", 'danger')
    return render_template("login.html", title="Login", form=form)


@users.route("/home")
def home():
    """ Home page route"""
    return render_template("home.html")
