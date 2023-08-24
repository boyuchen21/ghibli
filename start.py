from scrap_wallpaper import *
from get_movie_list import *

get_movie_list()
movie = input("Enter the English id for the movie you want to download wallpapers from: ")
scrap_wallpaper(movie)
