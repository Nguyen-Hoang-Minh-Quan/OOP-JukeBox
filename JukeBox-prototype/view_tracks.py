import tkinter as tk #Core tkinter library for GUI components
import tkinter.scrolledtext as tkst  #Scrolled text widget for displaying lists


import track_library as lib #Custom module to retrieve track information
import font_manager as fonts #Custom module to configure application fonts



def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class TrackViewer():
    def __init__(self, window): 
        window.geometry("750x350")  #Setup window dimensions and title
        window.title("View Tracks")

        #Button to display all tracks
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        #Label prompting user to enter a track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        #Construct a text field for the user to input a track number.
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        #Make a button that allows users to view the track's details.
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        #Make a scrolling text widget that shows every track.
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        #Create a text widget that displays the details of a single track.
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)


        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked()

    def view_tracks_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"
            set_text(self.track_txt, track_details)
        else:
            set_text(self.track_txt, f"Track {key} not found")
        self.status_lbl.configure(text="View Track button was clicked!")

    #Event handler: displays a list of all tracks in scrolled text area
    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

#Main entry point for the application
if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
