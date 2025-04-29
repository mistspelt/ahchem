from flask import Flask, redirect, Blueprint, url_for, current_app, flash
from flask_dance.contrib.google import make_google_blueprint, google
from app.auth import bp
from app import db
from app.models import User, oAuth
from flask_login import login_user, current_user, logout_user
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage
from sqlalchemy.orm.exc import NoResultFound

# create/login user on successful oauth
@oauth_authorized.connect
def google_logged_in(blueprint, token):
    if not token:
        flash("Failed to log in with Google.", category="error")
        return redirect(url_for("main.index"))
    
    resp = blueprint.session.get("/oauth2/v1/userinfo")
    if not resp.ok:
        flash("Failed to fetch user info from Google.", category="error")
        return redirect(url_for("main.index"))
    
    info = resp.json()
    user_id = info["id"]
    print("User ID:", user_id)

    # check if oauth already exists
    query = db.session.query(oAuth).filter_by(provider=blueprint.name, provider_user_id=user_id)
    try:
        oauth = query.one()
    except NoResultFound:
        oauth = oAuth(
            provider = blueprint.name,
            provider_user_id = user_id,
            token = token,
        )

    if oauth.user: # if it does, log in the user
        login_user(oauth.user)
        flash("Logged in successfully.", category="success")

    
    
    else:
        # create new user account
        
        email = info.get("email")
        if not email:
            flash("Failed to retrieve email from Google.", category="error")
            return False
        
        user = User(email=info["email"])
        oauth.user = user
        db.session.add_all([user, oauth])
        db.session.commit()

        # log in with new user account
        login_user(user)
        flash("Logged in successfully.", category="success")


    # disable flask dance automatic saving of token
    return False

# notify on oauth error
@oauth_error.connect
def google_error(blueprint, message, response):
    msg = (f"OAuth error from {blueprint.name}: {message} response: {response}")
    flash(msg, category="error")
