from tkinter import ttk, Label, Entry, Button, Listbox


class UpdateTrack:
    def __init__(self, notebook, library):
        self.library = library

        #Create tab
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="Update Track")

        #Create a Listbox to display songs
        Label(self.tab, text="Select Track:").grid(row=0, column=0, padx=10, pady=10)
        self.track_listbox = Listbox(self.tab, width=40, height=15)
        self.track_listbox.grid(row=1, column=0, padx=10, pady=10)

        # Load danh sách bài hát
        self.update_track_list()

        #Input boxes for song editing
        Label(self.tab, text="Track Name:").grid(row=2, column=0, padx=10, pady=10)
        self.name_entry = Entry(self.tab, width=40)
        self.name_entry.grid(row=2, column=1, padx=10, pady=10)

        Label(self.tab, text="Artist:").grid(row=3, column=0, padx=10, pady=10)
        self.artist_entry = Entry(self.tab, width=40)
        self.artist_entry.grid(row=3, column=1, padx=10, pady=10)

        Label(self.tab, text="YouTube URL:").grid(row=4, column=0, padx=10, pady=10)
        self.youtube_entry = Entry(self.tab, width=40)
        self.youtube_entry.grid(row=4, column=1, padx=10, pady=10)

        Label(self.tab, text="Rating (1-5):").grid(row=5, column=0, padx=10, pady=10)
        self.rating_entry = Entry(self.tab, width=40)
        self.rating_entry.grid(row=5, column=1, padx=10, pady=10)

        #"Update Track" button
        Button(self.tab, text="Update Track", command=self.update_track).grid(row=6, column=0, columnspan=2, pady=10)

    def update_track_list(self):
        self.track_listbox.delete(0, "end")
        for track_id, track in self.library.items():
            self.track_listbox.insert("end", f"{track_id}: {track.name}")

    def update_track(self):
        selected = self.track_listbox.curselection()
        if not selected:
            print("No track selected!")
            return

        #Get song ID
        track_id = list(self.library.keys())[selected[0]]

        #Update information
        name = self.name_entry.get().strip()
        artist = self.artist_entry.get().strip()
        youtube_url = self.youtube_entry.get().strip()
        rating = self.rating_entry.get().strip()

        if not rating.isdigit() or not (1 <= int(rating) <= 5):
            print("Invalid rating!")
            return

        self.library[track_id].name = name or self.library[track_id].name
        self.library[track_id].artist = artist or self.library[track_id].artist
        self.library[track_id].youtube_url = youtube_url or self.library[track_id].youtube_url
        self.library[track_id].rating = int(rating)

        print(f"Track '{self.library[track_id].name}' updated successfully!")
        self.update_track_list()
