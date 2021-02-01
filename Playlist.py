from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None
    self.songlist = []


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    song = Song(title)
    self.songlist.append(title)



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
      if title in self.songlist:
        return self.songlist.index(title)
      else:
        return -1


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    self.songlist.pop(self.songlist.index(title))



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    return len(self.songlist)


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    n = 1
    for i in range(len(self.songlist)): 
      print (f"{n}. {self.songlist[i]}") 
      n += 1
