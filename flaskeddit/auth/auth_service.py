from flask_login import login_user, logout_user, current_user
from passlib.hash import bcrypt

from flaskeddit import db
from flaskeddit.models import AppUser


def register_user(username, password):
    """
    Hashes the given password and registers a new user in the database.
    """
    hashed_password = bcrypt.hash(password)
    app_user = AppUser(username=username.lower(), password=hashed_password)
    db.session.add(app_user)
    db.session.commit()


def get_user(username):
    """
    Gets a post from a specified community by title from the database.
    """
    user = AppUser.query.filter_by(username=username).first()
    return user


def change_password(user, password):
    """
    Hashes the given password and registers a new user in the database.
    """
    hashed_password = bcrypt.hash(password)
    user.password = hashed_password
    db.session.commit()


def verify_password(password):

    if bcrypt.verify(password, current_user.password):
        return True
    else:
        return False



def log_in_user(username, password):
    """
    Hashes and compares the given password with the stored password. If it is a match,
    logs a user in.
    """
    app_user = AppUser.query.filter_by(username=username.lower()).first()
    if app_user and bcrypt.verify(password, app_user.password):
        login_user(app_user)
        return True
    else:
        return False


def log_out_user():
    """
    Logs the current user out.
    """
    logout_user()
