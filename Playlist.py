from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None
    self.songlist = []


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    if self.__first_song == None:
      self.__first_song = new_song
    else:
      current = self.__first_song
      while current._Song__next_song != None:
        current = current._Song__next_song
      current._Song__next_song = new_song

      



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current = self.__first_song
    index = 0
    while current._Song__title != title:
      if current._Song__next_song == None:
        return -1
      else:
        current = current._Song__next_song
        index += 1
    return index


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current = self.__first_song
    if current._Song__next_song == None:
      self.__first_song = None
    else:
      while current._Song__title != title:
        current = current._Song__next_song
      if current._Song__next_song == None:
        current = self.__first_song
        while current._Song__next_song._Song__title != title:
          current = current._Song__next_song
        current._Song__next_song = None
      else:
        current._Song__title = current._Song__next_song._Song__title
        current._Song__next_song = current._Song__next_song._Song__next_song
    

  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    current = self.__first_song
    index = 0
    if current != None:
      index = 1
      while current._Song__next_song != None:
        index += 1
        current = current._Song__next_song
    return index


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current = self.__first_song
    index = 0
    if current != None:
      index = 1
      print(str(index) + ". "  + current.get_title())
      while current._Song__next_song != None:
        current = current._Song__next_song
        index += 1
        print(str(index) + ". "  + current.get_title())

