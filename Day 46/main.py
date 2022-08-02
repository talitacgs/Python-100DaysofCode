import requests
from bs4 import BeautifulSoup
import os

MUSIC_URL = 'https://www.billboard.com/charts/hot-100/'
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f'{MUSIC_URL}{date}/'

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

music = soup.find_all(name='h3', class_='a-no-trucate')
name_song = [music_name.getText().replace('\n', '').replace('\t', '') for music_name in music]

data = {
    "name": "Python Playlist",
    "description": "New playlist description",
    "public": False,
}
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": os.environ.get("Authorization"),
}

user_id = os.environ.get('user_id')
create_playslit_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"

#create playlist
#response = requests.post(url=create_playslit_endpoint, json=data, headers=HEADERS)

playlist_id = os.environ.get("playlist_id")
position = 0

for track in name_song:
    track_name = f"{track}"
    search_track_endpoint = f"https://api.spotify.com/v1/search?q={track_name}&type=track&limit=1"
    response = requests.get(url=search_track_endpoint, headers=HEADERS)
    data_track = response.json()
    track_id = (data_track['tracks']['items'][0]['uri'].split(':')[2])
    add_song_playlist_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?position={position}&uris=spotify%3Atrack%3A{track_id}"
    try:
        response_post = requests.post(url=add_song_playlist_endpoint, headers=HEADERS)
        print(response_post)
    except:
        pass

