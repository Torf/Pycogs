import discogs_client as discogs
import sys
import os
import folder_object as folders


toAsk = []

class DiscogsApi(object):

  def __init__(self, verbose = False):
    self._verbose = verbose
    discogs.user_agent = 'Pytest/0.1 +http://ww.abc.fr'

  def searchSameArtistName(self, artistName):
    if self._verbose:
      print { "infos": 'Searching same artist name: %s' % artistName }

    s = discogs.NewSearch(artistName, 'artist')
    result = s.results()

    tries = 0

    for artist in result:
      if artist.name.strip().lower() == artistName.strip().lower():
        if self._verbose:
          print { "infos": 'Found same artist name: %s' % artist.name }
        return artist.name

      if ++tries > 10:
        return None

    return None

  def searchNearestArtistName(self, artistName):
    if self._verbose:
      print { "infos": 'Searching nearest artist name: %s' % artistName }

    s = discogs.NewSearch(artistName, 'artist')
    result = s.results()

    names = []
  
    for artist in result:
      if artist.name.strip().lower() == foldername.strip().lower():
        names.insert(0, artist.name)
      elif len(names) < 20:
        names.append(artist.name)
    
    return names

def main(args):
    
  musicFolder = "/medias/Musique/"

  genreList = { 'a':1}

  for artistDirName in os.listdir(musicFolder):
    artistFolder = folders.ArtistFolder(musicFolder, artistDirName)
    
    if not os.path.isdir(artistFolder.uri):
      continue
    
    print artistFolder

    for albumDirName in os.listdir(artistFolder.uri):
      albumFolder = folders.AlbumFolder(artistFolder, albumDirName)
      if not os.path.isdir(albumFolder.uri):
        continue
      #print albumFolder

      for musicFileName in os.listdir(albumFolder.uri):
        musicFile = folders.MusicFile(albumFolder, musicFileName)

        if os.path.isdir(musicFile.uri) or not musicFileName.endswith(".flac"):
          continue

        if musicFile.tags and "GENRE" in musicFile.tags:
          genre = musicFile.tags["GENRE"]
          if genre:
            genre = str(genre)
            if not genre in genreList.keys():
              genreList[genre] = 1
            else:
              genreList[genre] = genreList[genre] + 1

  print genreList

      
if __name__ == "__main__":
   main(sys.argv[1:])
  
