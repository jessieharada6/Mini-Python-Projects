from bs4 import BeautifulSoup
import requests
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

date = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD \n")

response = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12")
web_page_songs = response.text

soup = BeautifulSoup(web_page_songs, "html.parser")
songs_contents = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
songs_list = [song.getText() for song in songs_contents]

year = date.split("-")[0]
# spotify
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com",
#         client_id="YOUR UNIQUE CLIENT ID",
#         client_secret="YOUR UNIQUE CLIENT SECRET",
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user
# song_uris = []
# for song in songs_list:
#     result = sp.search(q=f"track:{song} year:{year}", type="track")
#     try:
#         uri = result["tracks"]["items"][0]["uri"]
#         song_uris.append(uri)
#     except IndexError:
#         print(f"{song} does not exist in Spotify. Skipped.")

# playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public = False)
# sp.playlist_add_items(playlist_id= playlist["id"], item=song_uris)