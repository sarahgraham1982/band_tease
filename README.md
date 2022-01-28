BAND TEASE

This app is an information resource for people who wear band t-shirts purely for fashion reasons and not because they are fans of the band. The user, when prompted to 'prove' they are worthy of wearing said t-shirt by a disgruntled, gate-keeping fan, can use this app for band trivia that only fans would know!

Instructions ///

Clone down the repo.

Install Flask (https://flask.palletsprojects.com/en/2.0.x/installation/).

Install psycopg2 (https://pypi.org/project/psycopg2/).

createdb band_tease

psql -d band_tease -f db/band_tease.sql

python3 console.py

q (to quit pdb)

flask run
