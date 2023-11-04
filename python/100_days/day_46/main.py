#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:44:05 2021
"""

import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.environ.get('SPOTIPY_REDIRECT_URI')
scope = "playlist-modify-private"
if not client_id or not client_secret or not redirect_uri:
    print("Please set SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI environment variables.")
    exit(1)

# Initialize the Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Test authentication
results = sp.current_user()
print("Authenticated as:", results['display_name'])

date = input(
    "Which year do you want to check? Type the date in this format YYYY-MM-DD: ")

# # Scrape Billboard Hot 100 for the given year
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(URL)
billboard_data = response.text
soup = BeautifulSoup(billboard_data, "html.parser")
songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")
song_titles = [title.getText().strip("\n\t") for title in songs]
artists = soup.find_all(name="span", class_="u-max-width-330")
artist_names = [name.getText().strip("\n\t") for name in artists]
song_and_artist = dict(zip(song_titles, artist_names))

print()

song_uris = {}

with open("songs.txt", "r") as file:
    for line in file:
        line = line.strip()
        if "-" in line:
            parts = line.split("-", 1)
            if len(parts) == 2:
                song_name, artist_name = map(str.strip, parts)
                try:
                    # Search for the song on Spotify
                    results = sp.search(q=f"track:{song_name} artist:{artist_name}", type="track", limit=1)

                    # Check if there are any search results
                    if results["tracks"]["total"] > 0:
                        # Get the Spotify URI of the first result
                        spotify_uri = results["tracks"]["items"][0]["uri"]
                        song_uris[song_name] = spotify_uri
                    else:
                        # Handle the case where the song was not found on Spotify
                        print(f"Song '{song_name}' by '{artist_name}' not found on Spotify.")
                except Exception as e:
                    print(f"Error occurred while searching for '{song_name}' by '{artist_name}': {str(e)}")
            else:
                print(f"Ignoring line with invalid format: {line}")
        else:
            print(f"Ignoring line with invalid format: {line}")

# Create a new private playlist
playlist_name = f"{date} Billboard 100"
playlist_description = f"Top 100 songs on {date}"
user_id = "31sywx24ynwbtunws2l6aajt7oqu"

# new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)
# print(f"Created playlist '{playlist_name}'.")
# playlist_id = new_playlist["id"]

# Add songs found on Spotify to the playlist
for song_name, spotify_uri in song_uris.items():
    sp.playlist_add_items(playlist_id=playlist_id, items=[spotify_uri])
print(f"Added {len(song_uris)} songs to the playlist.")
