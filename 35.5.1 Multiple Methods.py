class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []


    def add_song(self, song):
        self.songs.append(song)
        print(f"{song} added successfully...!")
    
    def remove_songs(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} successfully removed from the playlist...!")

    def show_songs(self):
        print(f"Play list name: {self.name}")
        for song in self.songs:
            print(f" - {song}")


my_playlist = Playlist("favourites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()