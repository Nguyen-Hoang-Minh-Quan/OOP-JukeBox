from tkinter import ttk, Label, Entry, Button
from track_library import LibraryItem


class CreateTrack:
    def __init__(self, notebook, library, view_track):
        self.library = library
        self.view_track = view_track  #Reference to ViewTrack

        #Create tab
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Create Track")

        #Enter song information
        Label(self.tab, text="Track Name:").grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = Entry(self.tab, width=40)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(self.tab, text="Artist:").grid(row=1, column=0, padx=10, pady=10)
        self.artist_entry = Entry(self.tab, width=40)
        self.artist_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(self.tab, text="YouTube URL:").grid(row=2, column=0, padx=10, pady=10)
        self.youtube_entry = Entry(self.tab, width=40)
        self.youtube_entry.grid(row=2, column=1, padx=10, pady=10)

        Label(self.tab, text="Rating (1-5):").grid(row=3, column=0, padx=10, pady=10)
        self.rating_entry = Entry(self.tab, width=40)
        self.rating_entry.grid(row=3, column=1, padx=10, pady=10)

        Label(self.tab, text="Image URL:").grid(row=4, column=0, padx=10, pady=10)
        self.image_entry = Entry(self.tab, width=40)
        self.image_entry.grid(row=4, column=1, padx=10, pady=10)

        #"Add Track" Button
        Button(self.tab, text="Add Track", command=self.add_track).grid(row=5, column=0, columnspan=2, pady=10)

    def add_track(self):
        name = self.name_entry.get().strip()
        artist = self.artist_entry.get().strip()
        youtube_url = self.youtube_entry.get().strip()
        rating = self.rating_entry.get().strip()
        image_url = self.image_entry.get().strip()

        if not name or not artist:
            print("Name and artist are required!")
            return

        if not rating.isdigit() or not (1 <= int(rating) <= 5):
            print("Rating must be a number between 1 and 5!")
            return

        new_id = str(len(self.library) + 1).zfill(2)
        self.library[new_id] = LibraryItem(name, artist, youtube_url, 0, int(rating), image_url)
        print(f"Track '{name}' added successfully!")

        #Reset input boxes
        self.name_entry.delete(0, "end")
        self.artist_entry.delete(0, "end")
        self.youtube_entry.delete(0, "end")
        self.rating_entry.delete(0, "end")
        self.image_entry.delete(0, "end")

        #Update ViewTrack
        self.view_track.update_track_list()
