from db.run_sql import run_sql

from models.band import Band
from models.user import User
import repositories.user_repository as user_repository

def save(band):
    sql = "INSERT INTO bands(band_name, genre, favourite_song, favourite_album, fun_fact, tee_image, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [band.band_name, band.genre, band.favourite_song, band.favourite_album, band.fun_fact, band.tee_image, band.user.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    band.id = id
    return band


def select_all ():
    bands = []

    sql = "SELECT * FROM bands"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        band = Band(row['band_name'], row['genre'], row['favourite_song'], row['favourite_album'], row['fun_fact'], row['tee_image'], user, ['id'])
        bands.append(band)
    return bands

   


def select(id):
    band = None
    sql = "SELECT * FROM bands WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = user_repository.select(result['user_id'])
        band = Band(result['band_name'], result['genre'], result['favourite_song'], result['favourite_album'], result['fun_fact'], result['tee_image'], user, result['id'])
    return band

def delete_all():
    sql = "DELETE FROM bands"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bands WHERE id = %s"
    values = [id]
    run_sql(sql, values)




def update(band):
    sql = "UPDATE bands SET (band_name, genre, favourite_song, favourite_album, fun_fact, tee_image) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [band.band_name, band.genre, band.favourite_song, band.favourite_album, band.fun_fact, band.tee_image, band.id]
    run_sql(sql, values)
