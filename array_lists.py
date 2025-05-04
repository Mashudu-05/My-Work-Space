class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Create a list called albums1 and add 5 albums to it
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Back in Black", 10, "AC/DC"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("The Wall", 26, "Pink Floyd"),
    Album("Hotel California", 9, "Eagles")
]

# Print albums1
print("Albums1:")
for album in albums1:
    print(album)

# Sort albums1 by number of songs and print it
albums1.sort(key=lambda x: x.number_of_songs)
print("\nAlbums1 sorted by number of songs:")
for album in albums1:
    print(album)

# Swap elements at position 1 and 2
albums1[1], albums1[2] = albums1[2], albums1[1]
print("\nAlbums1 after swapping elements at positions 1 and 2:")
for album in albums1:
    print(album)

# Create a new list called albums2
albums2 = []

# Add 5 albums to albums2
albums2.extend([
    Album("Born to Run", 8, "Bruce Springsteen"),
    Album("Let It Be", 12, "The Beatles"),
    Album("Nevermind", 12, "Nirvana"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Purple Rain", 9, "Prince")
])

print("\nAlbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 to albums2
albums2.extend(albums1)

# Add two new albums to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda x: x.album_name)
print("\nAlbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)

# Search for "Dark Side of the Moon" in albums2 and print its index
search_album = "Dark Side of the Moon"
index = next((i for i, album in enumerate(albums2) if album.album_name == search_album), -1)

print(f"\nIndex of '{search_album}' in albums2: {index}")