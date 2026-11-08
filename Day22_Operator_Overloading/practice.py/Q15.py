# Create a Playlist class and overload +, len(), and in.

# Requirements:

    # Store song names in a list.
    # Define __add__() to combine playlists.
    # Define __len__() to count songs.
    # Define __contains__() to search for songs.
    # Return a new Playlist when combining two playlists.
    # Test all three operations.

#----------------------------------------------------------------------------------------------------------


class Playlist:

    def __init__(self,name):
        self.name = name 

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)

    def __contains__(self, item):
        item in self.name
        print(item)


p1 = Playlist(["Shape of You", "Believer"])
p2 = Playlist(["Perfect", "Senorita"])

# +
p3 = p1 + p2
print("Combined Playlist:", p3)

# len()
print("Total Songs:", len(p3))

# in
print("Believer" in p3)
print("Havana" in p3)