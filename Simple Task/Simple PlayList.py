import tkinter as tk
from tkinter import messagebox

class PlaylistManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Playlist Manager")
        self.root.geometry("550x500")
        self.root.configure(bg="#2c3e50")

        # Variables
        self.playlist_name = tk.StringVar()
        self.song_name = tk.StringVar()

        # Build UI
        self.create_widgets()

    # =============================
    # UI SETUP
    # =============================
    def create_widgets(self):

        # Playlist name input
        tk.Label(self.root, text="Enter Playlist Name:",
                 bg="#2c3e50", fg="white").pack(pady=(20, 5)) # pady(20, 5) -> 20 pixels padding on top, 5 pixels padding on bottom
                # ↑ 20px gap above the widget, ↓  5px gap below the widget

        tk.Entry(self.root, textvariable=self.playlist_name).pack()

        tk.Button(self.root, text="Set Playlist Name",
                  command=self.update_playlist_name,
                  bg="#2980b9", fg="white").pack(pady=10)

        # Playlist label
        self.playlist_label = tk.Label(
            self.root, text="Playlist: None", bg="#2c3e50", fg="#ecf0f1")
        self.playlist_label.pack(pady=10)

        # Song name input
        tk.Label(self.root, text="Enter Song Name:",
                 bg="#2c3e50", fg="white").pack(pady=(10, 5))

        tk.Entry(self.root, textvariable=self.song_name).pack()

        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2c3e50")
        buttons_frame.pack(pady=15)

        tk.Button(buttons_frame, text="Add Song", command=self.add_song,
                  bg="#27ae60", fg="white", width=12).grid(row=0, column=0, padx=5)

        tk.Button(buttons_frame, text="Remove Song", command=self.remove_song,
                  bg="#c0392b", fg="white", width=12).grid(row=0, column=1, padx=5)

        tk.Button(buttons_frame, text="Show Songs", command=self.show_songs,
                  bg="#2980b9", fg="white", width=12).grid(row=0, column=2, padx=5)

        # Listbox
        self.song_listbox = tk.Listbox(self.root, bg="#34495e",
                                       fg="white", height=10)
        self.song_listbox.pack(padx=20, pady=10, fill="both", expand=True)

    # =============================
    # LOGIC FUNCTIONS (Methods)
    # =============================
    def update_playlist_name(self):
        name = self.playlist_name.get().strip()

        if name == "":
            messagebox.showwarning("Input Error", "Please enter a playlist name.")
            return

        self.playlist_label.config(text="Playlist: " + name)

    def playlist_is_set(self):
        return self.playlist_name.get().strip() != ""

    def add_song(self):
        if not self.playlist_is_set():
            messagebox.showwarning("Playlist Missing", "Set playlist name first!")
            return

        song = self.song_name.get().strip()

        if song == "":
            messagebox.showwarning("Input Error", "Please enter a song name.")
            return

        self.song_listbox.insert(tk.END, song)
        self.song_name.set("")

    def remove_song(self):
        if not self.playlist_is_set():
            messagebox.showwarning("Playlist Missing", "Set playlist name first!")
            return

        song = self.song_name.get().strip()
        selected = self.song_listbox.curselection()

        # If user typed a song name
        if song != "":
            all_songs = self.song_listbox.get(0, tk.END)
            if song not in all_songs:
                messagebox.showerror("Not Found", f'"{song}" not found.')
                return

            # Remove all occurrences
            i = 0
            while i < self.song_listbox.size():
                if self.song_listbox.get(i) == song:
                    self.song_listbox.delete(i)
                else:
                    i += 1

            messagebox.showinfo("Song Removed", f'"{song}" removed.')
            self.song_name.set("")
            return

        # If user selected from the listbox
        if not selected:
            messagebox.showwarning("Error", "Select a song or type name.")
            return

        for i in reversed(selected):
            self.song_listbox.delete(i)

    def show_songs(self):
        if not self.playlist_is_set():
            messagebox.showwarning("Playlist Missing", "Set playlist name first!")
            return

        songs = self.song_listbox.get(0, tk.END)

        if songs:
            messagebox.showinfo("Songs", "\n".join(songs))
        else:
            messagebox.showinfo("Songs", "No songs in playlist.")


# =============================
# RUN THE APPLICATION
# =============================
root = tk.Tk()
app = PlaylistManagerApp(root)
root.mainloop()