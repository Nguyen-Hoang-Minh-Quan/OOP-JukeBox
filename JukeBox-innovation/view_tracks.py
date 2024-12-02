from tkinter import ttk, Listbox, Label
import tkinter.scrolledtext as tkst


class ViewTrack:
    def __init__(self, notebook, library, open_youtube_func):
        self.library = library
        self.open_youtube_func = open_youtube_func

        #Create tabs
        self.tab = ttk.Frame(notebook)
        notebook.add(self.tab, text="View Tracks")

        #ScrolledText to display song information
        self.view_track_text = tkst.ScrolledText(self.tab, width=60, height=15, state="disabled")
        self.view_track_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        #Listbox displays song names
        self.track_listbox = Listbox(self.tab, width=40, height=15)
        self.track_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        #Frame to display rating
        self.info_frame = ttk.Frame(self.tab)
        self.info_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

        #Display rating as Unicode symbols
        self.rating_label = Label(self.info_frame, text="", font=("Helvetica", 16))
        self.rating_label.pack()

        # Nút để mở bài hát trên YouTube
        self.open_button = ttk.Button(self.tab, text="Open on YouTube", command=self.open_selected_track)
        self.open_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        #Load the song into the list
        self.update_track_list()

        #Enhanced interface grid
        self.tab.grid_rowconfigure(0, weight=1)
        self.tab.grid_rowconfigure(1, weight=1)
        self.tab.grid_columnconfigure(0, weight=1)
        self.tab.grid_columnconfigure(1, weight=0)

    def update_track_list(self):
        self.track_listbox.delete(0, "end")
        for track_id, track in self.library.items():
            self.track_listbox.insert("end", f"{track.name} (Rating: {track.rating})")

    def display_rating(self, rating):
        full_stars = "★" * rating
        empty_stars = "☆" * (5 - rating)
        self.rating_label.config(text=full_stars + empty_stars)

    def open_selected_track(self):
        selected = self.track_listbox.curselection()
        if not selected:
            return

        track_id = list(self.library.keys())[selected[0]]
        track = self.library[track_id]

        #Show the rating
        self.display_rating(track.rating)

        #Open YouTube
        self.open_youtube_func(track.name, self.library)
