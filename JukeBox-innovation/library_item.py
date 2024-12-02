#Class LibraryItem defines a song in the library
class LibraryItem:
    def __init__(self, name, artist, youtube_url, play_count=0, rating=0):
        self.name = name
        self.artist = artist
        self.youtube_url = youtube_url
        self.play_count = play_count
        self.rating = rating

    def info(self):
        """Trả về thông tin về bài hát."""
        return f"{self.name} by {self.artist} | Rating: {self.rating} | Played: {self.play_count} times"
