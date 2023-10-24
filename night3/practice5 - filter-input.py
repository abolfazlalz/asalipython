def artist_input(text):
  artists = ['yas', 'tatalo', 'hiphopologist', 'Mehrad Hidden']
  artist_name = input(text)

  # use if condition
  if artist_name not in artists:
    # use recursive method
    return artist_input(text)

  # return final variable
  return artist_name

artist = artist_input("Enter artist name:")
print(artist)