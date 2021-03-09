songs_list = [("Uptown Funk", "Mark Ronson"),
         ("Thinking Out Loud", "Ed Sheeran"),
         ("Sugar", "Maroon 5"),
         ("Patterns In The Ivy", "Opeth"),
         ("Take Me To Church", "Hozier"),
         ("Style", "Taylor Swift"),
         ("Love Me Like You Do", "Ellie Goulding")]

artists = set()

for song, artist in songs_list:
    artists.add(artist)

print(artists)


songs = {'Style', 'Uptown Funk', 'Take Me To Church', 'Sugar',
                 'Thinking Out Loud', 'Patterns In The Ivy', 'Love Me Like You Do'}

print(songs)
print("Sugar" in songs)

for artist in artists:
    print(f"{artist} plays excellent music.")


## Ordered lists from sets

artists_list = list(artists)
artists_list.sort()
print(artists_list)


# As mathematical structures

my_artists = {
               'Hozier', 'Opeth', 'Ellie Goulding', 'Mark Ronson', 'Taylor Swift'}

artists_album = {'Maroon 5', 'Taylor Swift', 'Amy Wadge'}


# Union

print(f"All: {my_artists.union(artists_album)}")

# Intersection

print(f"Both: {my_artists.intersection(artists_album)}")

# Difference

print("Only in A: {}".format(my_artists.difference(artists_album)))


# Symmetric difference

print("Any but not both: {}".format(my_artists.symmetric_difference(artists_album)))



print("-"*20)

bands = {"Opeth", "Guns N' Roses"}

print("my artist is to bands: ")

print("issuperset: {}".format(my_artists.issuperset(bands)))
print("issubset: {}".format(my_artists.issubset(bands)))
print("difference: {}".format(my_artists.difference(bands)))

print("-"*20)
print("bands is to my_artists:")
print("issuperset: {}".format(bands.issuperset(my_artists)))
print("issubset: {}".format(bands.issubset(my_artists)))
print("difference: {}".format(bands.difference(my_artists)))



              
               
                



