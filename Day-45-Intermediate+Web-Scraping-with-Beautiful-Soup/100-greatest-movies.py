from bs4 import BeautifulSoup
import requests

response = requests.get("https://stacker.com/stories/1587/100-best-movies-all-time")
movie_page = response.text

soup = BeautifulSoup(movie_page, "html.parser")
films = []
film_contents = soup.find_all(name="h2", class_="ct-slideshow__slide__text-container__caption")

films = [film.getText().replace("\n", "").replace("#", "") for film in film_contents]
films.pop(0)
# reverse list
reversed_films = films[::-1]

print(reversed_films)

with open("100_top_films.txt", mode="w") as file:
    # write each string to the file
    for film in reversed_films:
        file.write(film + "\n")
