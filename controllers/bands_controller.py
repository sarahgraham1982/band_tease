from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.bands import Band
import repositories.band_repository as band_repository
import repositories.user_repository as user_repository

bands_blueprint = Blueprint("bands", __name__)

@bands_blueprint.route("/bands")
def bands():
    bands = band_repository.select_all()
    return render_template("bands/index.html", all_bands = bands)

# CRUD

@bands_blueprint.route("/bands/new", methods=['GET'])
def new_band():
    users = user_depository.select_all()
    return render_template("bands/new.html", all_users = users)

@bands_blueprint.route("/bands", methods=['POST'])
def create_band():
    


