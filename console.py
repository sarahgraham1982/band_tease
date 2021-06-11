import pdb
from models.band import Band
from models.user import User

import repositories.band_repository as band_repository
import repositories.user_repository as user_repository
import repositories.user_band_repository as user_band_repository

band_repository.delete_all()
user_repository.delete_all()
user_band_repository.delete_all()

user1 = User("Kendall")
user_repository.save(user1)
user2 = User("Justin")
user_repository.save(user2)

user_repository.select_all()

band1 = Band("Slayer", "Thrash Metal", "Black Magic", "Show No Mercy", "Last UK gig was in Glasgow in November 2018.", user1)
band_repository.save(band1)
band2 = Band("Nirvana", "Grunge", "Serve the Servants", "In Utero", "Lead singer died from a gunshot in 1994.", user2)
band_repository.save(band2)

band_repository.select_all()

user_band1 = UserBand(user1, band1)
user_band_repository.save(user_band1)
user_band2 =UserBand(user2, band2)
user_band_repository.save(user_band2)

pdb.set_trace()