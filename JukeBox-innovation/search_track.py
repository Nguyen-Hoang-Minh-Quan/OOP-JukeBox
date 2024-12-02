# search_track.py
from track_library import library
import webbrowser

def open_youtube_from_name(song_name):
    for key, track in library.items():
        if song_name.lower() in track.name.lower():
            if track.youtube_url:
                webbrowser.open(track.youtube_url)
                return track.youtube_url
    return "Song not found"
