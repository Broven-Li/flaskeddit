from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from passlib.hash import bcrypt

from flaskeddit.auth import auth_blueprint, auth_service
from flaskeddit import db
from flaskeddit.models import AppUser
from flaskeddit.auth.forms import LoginForm, RegisterForm, ChangePasswordForm


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    """
    Route for registering new users. On a GET request, it returns the registration
    form. On a POST request, it handles user registration.
    """
    if current_user.is_authenticated:
        return redirect(url_for("feed.feed"))
    form = RegisterForm()
    if form.validate_on_submit():
        auth_service.register_user(form.username.data, form.password.data)
        flash("Successfully registered.", "primary")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    """
    Route for logging in users. On a GET request, it returns the login form. On a POST
    request, it handles user login.
    """
    if current_user.is_authenticated:
        return redirect(url_for("feed.feed"))
    form = LoginForm()
    if form.validate_on_submit():
        login_successful = auth_service.log_in_user(
            form.username.data, form.password.data
        )
        if login_successful:
            flash("Successfully logged in.", "primary")
            next_location = request.args.get("next")
            if next_location is None or not next_location.startswith("/"):
                next_location = url_for("feed.feed")
            return redirect(next_location)
        else:
            flash("Login Failed", "danger")
            return redirect(url_for("auth.login"))
    return render_template("login.html", form=form)


@auth_blueprint.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """
    Route for logging out current users.
    """
    auth_service.log_out_user()
    flash("Successfully logged out.", "primary")
    return redirect(url_for("auth.login"))


@auth_blueprint.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """
    Route for registering new users. On a GET request, it returns the registration
    form. On a POST request, it handles user registration.
    """
    username = current_user.username
    user = auth_service.get_user(username)
    form = ChangePasswordForm()
    if form.validate_on_submit():
        old_password = form.old_password.data
        if auth_service.verify_password(old_password):
            #current_user.password = form.password.data
            #user = AppUser.query.filter(AppUser.username == current_user.username).first()
            #print (user.password)
           # user.password = bcrypt.hash(current_user.password)
           # print(user.password)
           # db.session.add(user)
           # db.session.commit
           # print(current_user.password)
            # 加入数据库的session，这里不需要.commit()，在配置文件中已经配置了自动保存

            auth_service.change_password(user, form.password.data)
            flash("Successfully changed.", "primary")
            return redirect(url_for('auth.login'))
        else:
            flash("Invalid password.", "danger")
    return render_template("change_password.html", form=form)
