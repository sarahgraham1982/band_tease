import pdb
from models.band import Band
from models.user import User


import repositories.band_repository as band_repository
import repositories.user_repository as user_repository


band_repository.delete_all()
user_repository.delete_all()


user1 = User("Kendall", "Jenner")
user_repository.save(user1)
user2 = User("Justin", "Bieber")
user_repository.save(user2)

user_repository.select_all()

band1 = Band("Slayer", "Thrash Metal", "Black Magic", "Show No Mercy", "Last UK gig was in Glasgow in November 2018.", "slayer_tee.jpeg", user1)
band_repository.save(band1)

band2 = Band("Nirvana", "Grunge", "Serve the Servants", "In Utero", "Lead singer died from a gunshot in 1994.", "nirvana_tee.jpeg", user2)
band_repository.save(band2)

band3 = Band("Metallica", "Heavy Metal", "Fuel", "Reload", "Regarded as one of the 'Big Four' along with Slayer, Anthrax and Megadeath.", "metallica_tee.jpeg", user2)
band_repository.save(band3)

band4 = Band("Iron Maiden", "Heavy Metal", "The Wicker Man", "Brave New World", "They have a skeleton mascot called Eddie who appears in all their album cover artwork.", "iron_maiden_tee.jpeg", user2)
band_repository.save(band4)

band5 = Band("AC/DC", "Hard Rock", "Thunderstruck", "The Razor's Edge", "Founding members, brothers Brian and Angus were both born in Scotland.", "acdc_tee.jpeg", user1)
band_repository.save(band5)

band6 = Band("T-Rex", "Glam Rock", "Debora", "Electric Warrior", "They headlined the first ever Glastonbury.", "t_rex_tee.jpeg", user1)
band_repository.save(band6)


band_repository.select_all()


pdb.set_trace()