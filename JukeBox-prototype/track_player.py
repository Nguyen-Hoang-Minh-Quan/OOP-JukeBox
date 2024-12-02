import tkinter as tk

# Import other necessary modules (replace these with actual imports)
import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import CreateTrackList
from update_tracks import UpdateTracks

class JukeBoxApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("520x350")  # Set geometry for the main window
        self.window.title("JukeBox")
        self.window.configure(bg="gray")
        
        fonts.configure()
        
        self.create_main_frame()  # Initialize main frame
    
    def create_main_frame(self):
        """Create and display the main frame."""
        self.main_frame = tk.Frame(self.window, bg="lightgray")
        self.main_frame.pack(fill="both", expand=True)

        header_lbl = tk.Label(self.main_frame, text="Select an option by clicking one of the buttons below", font=("Helvetica", 14))
        header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Buttons for the options
        view_tracks_btn = tk.Button(self.main_frame, text="View Tracks", command=self.view_tracks_clicked)
        view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        create_track_list_btn = tk.Button(self.main_frame, text="Create Track List", command=self.create_tracks_list)
        create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

        update_tracks_btn = tk.Button(self.main_frame, text="Update Tracks", command=self.update_tracks)
        update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(self.main_frame, bg='gray', text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
    def view_tracks_clicked(self):
        """Handle the 'View Tracks' button click."""
        self.status_lbl.configure(text="View Tracks button was clicked!")
        TrackViewer(tk.Toplevel(self.window))  # Open a new window for track viewer
    
    def create_tracks_list(self):
        """Handle the 'Create Track List' button click."""
        self.status_lbl.configure(text="Create Track List button clicked!")
        CreateTrackList(tk.Toplevel(self.window))  # Open a new window to create track list
    
    def update_tracks(self):
        """Handle the 'Update Tracks' button click."""
        self.status_lbl.configure(text="Update Tracks button clicked!")
        UpdateTracks(tk.Toplevel(self.window))  # Open a new window to update track list

# Initialize the main window
window = tk.Tk()

# Create an instance of the JukeBoxApp class
app = JukeBoxApp(window)

# Start the main loop
window.mainloop()
