from db.run_sql import run_sql

from models.band import Band
from models.user import User
import repositories.user_repository as user_repository


def save(band):
