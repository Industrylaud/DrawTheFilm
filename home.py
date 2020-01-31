from filmweb.filmweb import Filmweb
from filmweb.items import User
from filmweb.items import Film
import random


def logIn(login, password):
    fw = Filmweb()
    fw.login(login, password)
    return fw


def rollFilm(fw):
    user = User(fw)
    id_list = []
    for film in user.get_want_to_see():
        id_list.append(film.get('film').uid)
    random_id_film = random.choice(id_list)
    return Film(fw, random_id_film)


def getName(randomedFilm):
    return randomedFilm.get_info().get('name')


#base = logIn('mrfros22', 'poziomal22')
#print(getName(rollFilm(base)))
#print(getPoster(rollFilm(base)))

