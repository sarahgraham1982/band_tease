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
user3 = User("Miley", "Cyrus")
user_repository.save(user3)

user_repository.select_all()

band1 = Band("SLAYER", "Thrash Metal", "Black Magic", "Show No Mercy", "Last UK gig was in Glasgow in November 2018.", "slayer_tee.png", user1)
band_repository.save(band1)

band2 = Band("NIRVANA", "Grunge", "Serve the Servants", "In Utero", "Lead singer died from a gunshot in 1994.", "nirvana_tee.png", user2)
band_repository.save(band2)

band3 = Band("METALLICA", "Heavy Metal", "Fuel", "Reload", "Regarded as one of the 'Big Four' along with Slayer, Anthrax and Megadeath.", "metallica_tee.png", user2)
band_repository.save(band3)

band4 = Band("IRON MAIDEN", "Heavy Metal", "The Wicker Man", "Brave New World", "They have a skeleton mascot called Eddie who appears in all their album cover artwork.", "iron_maiden_tee.png", user2)
band_repository.save(band4)

band5 = Band("AC/DC", "Hard Rock", "Thunderstruck", "The Razor's Edge", "Founding members, brothers Brian and Angus were both born in Scotland.", "acdc_tee.png", user1)
band_repository.save(band5)

band6 = Band("T-REX", "Glam Rock", "Debora", "Electric Warrior", "They headlined the first ever Glastonbury.", "t_rex_tee.png", user1)
band_repository.save(band6)


band7 = Band("BLACK FLAG", "Punk Rock", "Rise Above", "Damaged", "The guitarist Greg Ginn wrote most of their songs.", "black_flag_tee.png", user3)
band_repository.save(band7)

band8 = Band("GUNS N' ROSES", "Rock", "Nightrain", "Appetite for Destruction", "Lead singer Axl Rose hates performing live and often turns up late to their shows.", "gnr_tee.png", user3)
band_repository.save(band8)

band9 = Band("THE SMITHS", "Indie", "Still Ill", "The Queen is Dead", "Lead singer, Morrissey, although a good singer, has problematic views.", "smiths_tee.png", user3)
band_repository.save(band9)


band_repository.select_all()


pdb.set_trace()