import webbrowser
import json


class LibraryItem:
    def __init__(self, name, artist, youtube_url, play_count=0, rating=0, image_url=""):
        self.name = name
        self.artist = artist
        self.youtube_url = youtube_url
        self.play_count = play_count
        self.rating = rating
        self.image_url = image_url  #URL or path to the image

    def info(self):
        return f"{self.name} by {self.artist} | Rating: {self.rating} | Played: {self.play_count} times"


def open_youtube_from_name(song_name, library):
    for track in library.values():
        if song_name.lower() in track.name.lower():
            if track.youtube_url:
                webbrowser.open(track.youtube_url)
                return track.youtube_url
    return "Song not found in the library."


def load_songs_from_json(filename):
    library = {}
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for key, song in data.items():
                track = LibraryItem(
                    name=song["name"],
                    artist=song["artist"],
                    youtube_url=song["youtube_url"],
                    rating=song.get("rating", 0),
                    image_url=song.get("image_url", "")
                )
                library[key] = track
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: JSON parsing failed. Details: {e}")
    return library

