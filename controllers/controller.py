

from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.band import Band
import repositories.band_repository as band_repository
import repositories.user_repository as user_repository

bands_blueprint = Blueprint("bands", __name__)

# @bands_blueprint.route("/")
# def home():
#     return render_template("index.html")


@bands_blueprint.route("/bands")
def bands():
    bands = band_repository.select_all()
    # print([vars(item) for item in bands])
    return render_template("bands/index.html", bands = bands)

# NEW
# GET '/bands/new'
@bands_blueprint.route("/bands/new", methods=['GET'])
def new_band():
    users = user_repository.select_all()
    return render_template("bands/new.html", all_users = users)
    # changed users to all_users

# CREATE
# POST '/bands' 
@bands_blueprint.route("/bands", methods=['POST'])
def create_band():
    band_name           = request.form['band_name']
    user_id             = request.form['user_id']
    genre               = request.form['genre']
    favourite_song      = request.form['favourite_song']
    favourite_album     = request.form['favourite_album']
    fun_fact            = request.form['fun_fact']
    tee_image           = "default.png"
    user                = user_repository.select(user_id)
    band                = Band(band_name, genre, favourite_song, favourite_album, fun_fact, tee_image, user)
    band_repository.save(band)
    return redirect('/bands') 

# SHOW
# GET '/bands/<id>'
@bands_blueprint.route("/bands/<id>", methods=['GET'])
def show_band(id):
    band = band_repository.select(id)
    return render_template('bands/show.html', band = band)

# EDIT
# GET '/bands/<id>/edit'
@bands_blueprint.route("/bands/<id>/edit", methods=['GET'])
def edit_band(id):
    band = band_repository.select(id)
    users = user_repository.select_all()
    return render_template('bands/edit.html', band = band, all_users = users)

# UPDATE
# PUT '/bands/<id>'
@bands_blueprint.route("/bands/<id>", methods=['POST'])
def update_band(id):
    band_name           = request.form['band_name']
    user_id             = request.form['user_id']
    genre               = request.form['genre']
    favourite_song      = request.form['favourite_song']
    favourite_album     = request.form['favourite_album']
    fun_fact            = request.form['fun_fact']
    tee_image           = "default.png" 
    user                = user_repository.select(user_id)
    band                = Band(band_name, genre, favourite_song, favourite_album, fun_fact, tee_image, user, id)
    band_repository.update(band)
    return redirect('/bands') 

# DELETE
# DELETE '/bands/<id>'
@bands_blueprint.route("/bands/<id>/delete", methods=['POST'])
def delete_band(id):
    band_repository.delete(id)
    return redirect('/bands')







