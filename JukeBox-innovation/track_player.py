import os
import tkinter as tk
from tkinter import ttk
from view_tracks import ViewTrack
from create_track_list import CreateTrack
from update_tracks import UpdateTrack
from track_library import open_youtube_from_name, load_songs_from_json


class JukeboxApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Jukebox")

        # Ensure the working directory is set to the script's location
        script_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_directory)

        # Load songs from the JSON file
        json_file_path = os.path.join(script_directory, 'songs.json')
        self.library = load_songs_from_json(json_file_path)

        # Create a notebook widget (for tabs)
        self.notebook = ttk.Notebook(window)
        self.notebook.pack(expand=1, fill="both")

        # Initialize tabs for viewing, creating, and updating tracks
        self.view_track_tab = ViewTrack(self.notebook, self.library, open_youtube_from_name)
        self.create_track_tab = CreateTrack(self.notebook, self.library, self.view_track_tab)
        self.update_track_tab = UpdateTrack(self.notebook, self.library)


if __name__ == "__main__":
    root = tk.Tk()
    app = JukeboxApp(root)
    root.mainloop()
