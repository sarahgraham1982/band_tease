from db.run_sql import run_sql

from models.user import User
from models.band import Band

def save(user):
    sql = "INSERT INTO users (user_name) VALUES (%s) RETURNING *"
    values = [user.user_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    return user

def select_all():
    users = []

    sql = "SELECT * FROM users"
    results = run_sql(sql)

    for row in results:
        user = User(row['user_name'], row['id'])
        users.append(user)
    return users

def select(id):
    user = None
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        user = User(result['user_name'], result['id'])
    return user

def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(user):
    sql = "UPDATE users SET (user_name) = (%s) WHERE id = %s"
    values = [user.user_name, user.id]
    run_sql(sql, values)

def bands(user):
    bands = [] 

    sql = "SELECT * FROM bands WHERE user_id = %s"
    values = [user.id]
    results = run.sql, (sql, values)

    for row in results:
        band = Band(row['band_name'], row['genre'], row['favourite_song'], row['favourite_album'], row['fun_fact'], row['id'])
        bands.append(band)
    return bands