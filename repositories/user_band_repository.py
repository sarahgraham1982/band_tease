from db.run_sql import run.sql

from models.user_ands import UserBand
from models.band import Band
from models.user import User

import repositories.user_repository as user_repository
import repositories.band_repository as band_repository

def save(user_band):
    sql = "INSERT INTO users_bands(user_id, band_id) VALUES (%s, %s) RETURNING id"
    values = [user_band.user.id, user_band.band.id]
    results = run_sql(sql, values)
    user_band.id = results[0]['id']
    return user_band

def select_all():
    users_bands = []

    sql = "SELECT = * FROM users_bands"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        band = band_repository.select(row['band_id'])
        user_band = UserBand(user, band, row['id'])
        users_bands.append(user_band)
    return users_bands

def band(user_band):
    sql = "SELECT * FROM bands WHERE id = %s"
    values = [user_band.band.id]
    results = run_sql(sql, values)[0]
    band = Band(results['band_name'], results['genre'], results['favourite_song'], results['favourite_album'], results['fun_fact'], results['id'])
    return band

def user(user_band):
    sql = "SELECT * FROM users WHERE id = %s"
    values = [user_band.user.id]
    results - run_sql(sql, values)[0]
    user = User(results['name'], results['id'])
return user

def delete_all():
    sql = "DELETE FROM users_bands"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users_bands WHERE id = %s"
    values = [id]
    run_sql(sql, values)

